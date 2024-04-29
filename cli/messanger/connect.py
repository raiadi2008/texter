import paramiko

from cli.encrypter.encrypt_decrypt import encrypt_message
from cli.encrypter.keygen import generate_key_pair


def read_public_key(recipient_public_key_path):
    with open(recipient_public_key_path, "rb") as key_file:
        return key_file.read()


def create_connection(ip_address, recipient_public_key_path: str):
    private_key_pem, public_key_pem = generate_key_pair()
    recipient_public_key_pem = read_public_key(recipient_public_key_path)
    encrypted_public_key = encrypt_message(public_key_pem, recipient_public_key_pem)
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(ip_address, username="root")
    ssh_client.exec_command(f"echo '{encrypted_public_key.decode()}' > /root/.ssh/authorized_keys")
    return ssh_client
