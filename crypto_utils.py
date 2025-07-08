from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import base64
import os

def generate_key_from_password(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100_000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt_note(note: str, password: str) -> bytes:
    salt = os.urandom(16)
    key = generate_key_from_password(password, salt)
    f = Fernet(key)
    encrypted = f.encrypt(note.encode())
    return salt + encrypted

def decrypt_note(data: bytes, password: str) -> str:
    salt = data[:16]
    encrypted = data[16:]
    key = generate_key_from_password(password, salt)
    f = Fernet(key)
    return f.decrypt(encrypted).decode() 