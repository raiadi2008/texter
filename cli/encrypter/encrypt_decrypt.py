from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding


def encrypt_message(message, recipient_public_key_pem):
    public_key = serialization.load_pem_public_key(
        recipient_public_key_pem,
        backend=default_backend()
    )
    encrypted_message = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_message


def decrypt_message(message, private_key_pem, passphrase):
    private_key = serialization.load_pem_private_key(
        private_key_pem,
        password=passphrase.encode(),
        backend=default_backend()
    )
    decrypted_message = private_key.decrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_message.decode()
