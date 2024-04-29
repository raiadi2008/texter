from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa


def generate_key_pair(passphrase: str = None):
    private_key_path = "private_key.pem"
    public_key_path = "public_key.pem"

    try:
        with open(private_key_path, "rb") as key_file:
            private_key_pem = key_file.read()
        with open(public_key_path, "rb") as key_file:
            public_key_pem = key_file.read()
        return private_key_pem, public_key_pem
    except FileNotFoundError:
        print("here")

    print("restarting")
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    if passphrase:
        encryption_algorithm = serialization.BestAvailableEncryption(passphrase.encode())
    else:
        encryption_algorithm = serialization.NoEncryption()

    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=encryption_algorithm
    )
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open(private_key_path, "wb") as key_file:
        key_file.write(private_key_pem)
    with open(public_key_path, "wb") as key_file:
        key_file.write(public_key_pem)

    return private_key_pem, public_key_pem
