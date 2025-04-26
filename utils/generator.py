import secrets
import string

def generate_password(length=16, use_symbols=True):
    chars = string.ascii_letters + string.digits
    if use_symbols:
        chars += "!@#$%^&*()_+=[]{}|;:,.<>?"
    return ''.join(secrets.choice(chars) for _ in range(length))

