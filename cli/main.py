import argparse
from getpass import getpass
from ..core.vault import Vault
from ..utils.generator import generate_password

def main():
    vault = Vault()
    parser = argparse.ArgumentParser(description="SafePass CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Initialize vault
    init_parser = subparsers.add_parser("init", help="Create a new vault")

    # Unlock vault
    unlock_parser = subparsers.add_parser("unlock", help="Unlock the vault")

    # Add entry
    add_parser = subparsers.add_parser("add", help="Add a password entry")
    add_parser.add_argument("--name", required=True)
    add_parser.add_argument("--username", required=True)

    args = parser.parse_args()

    if args.command == "init":
        password = getpass("Set master password:")
        vault.initialize_vault(password)
        print("Vault created.")

    elif args.command == "unlock":
        password = getpass("Master password:")
        vault.unlock_vault(password)
        print("Vault unlocked.")

if __name__ == "__main__":
    main()
