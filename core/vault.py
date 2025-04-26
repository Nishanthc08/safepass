import json
import os
from threading import Timer
from .crypto import derive_key, encrypt_data, decrypt_data

VAULT_PATH = os.path.expanduser("~/.local/share/safepass/vault.enc")

class Vault:
    def __init__(self):
        self.vault_data = {} # {id: {name, username, password, url, notes}}
        self.is_locked = True
        self.salt = None
        self.key = None
        self.lock_timer = None

    def initialize_vault(self, master_password: str):
        """Create a new encrypted vault."""
        self.salt = os.urandom(16)
        self.key = derive_key(master_password, self.salt)
        self.vault_data = {"entries": {}}
        self._save_vault()
        self.is_locked = False

    def unlock_vault(self, master_password: str):
        """Decrypt the vault using the master password."""
        with open(VAULT_PATH, "rb") as f:
            self.salt = f.read(16)
            encrypted_data = f.read()
        self.key = derive_key(master_password, self.salt)
        decrypted = decrypt_data(encrypted_data, self.key)
        self.vault_data = json.loads(decrypted)
        self.is_locked = False
        self._reset_lock_timer()

    def _save_vault(self):
        """Encrypt and save vault data to disk."""
        data = json.dumps(self.vault_data).encode()
        encrypted = encrypt_data(data, self.key)
        os.makedirs(os.path.dirname(VAULT_PATH), exist_ok=True)
        with open(VAULT_PATH, "wb") as f:
            f.write(self.salt + encrypted)
        os.chmod(VAULT_PATH, 0o600) # Restricted permissions

    def _reset_lock_timer(self, timeout=300):
        """Reset auto-lock timer on user activity."""
        if self.lock_timer:
            self.lock_timer.cancel()
        self.lock_timer = Timer(timeout, self.lock_vault)
        self.lock_timer.start()

    def lock_vault(self):
        """Clear sensitive data from memory."""
        self.key = None
        self.vault_data = {}
        self.is_locked = True
    
