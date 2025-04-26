from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import os

def derive_key(password: str, salt: bytes) -> bytes:
    """Derive a 32-bit key from a password and salt."""
    kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=480000,
    )
    return kdf.derive(password.encode())

def encrypt_data(data: bytes, key: bytes) -> bytes:
    """Encrypt data with Fernet"""
    return Fernet(key).encrypt(data)

def decrypt_data(encrypted_data: bytes, key: bytes) -> bytes:
    """Decrypt Fernet-encrypted data."""
    return Fernet(key).decrypt(encrypted_data)

