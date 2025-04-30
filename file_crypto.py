# file_crypto.py

from cryptography.fernet import Fernet
import os

# --- Generate a key and save to file ---
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("[✓] Key generated and saved to secret.key")

# --- Load key from file ---
def load_key():
    try:
        with open("secret.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        print("[!] Key file not found. Generate a key first.")
        return None

# --- Encrypt file content ---
def encrypt_file(input_file, output_file):
    key = load_key()
    if not key:
        return
    fernet = Fernet(key)

    with open(input_file, "rb") as f:
        data = f.read()

    encrypted = fernet.encrypt(data)

    with open(output_file, "wb") as f:
        f.write(encrypted)

    print(f"[✓] File '{input_file}' encrypted and saved as '{output_file}'")

# --- Decrypt file content ---
def decrypt_file(input_file, output_file):
    key = load_key()
    if not key:
        return
    fernet = Fernet(key)

    with open(input_file, "rb") as f:
        data = f.read()

    try:
        decrypted = fernet.decrypt(data)
    except Exception as e:
        print("[!] Decryption failed:", str(e))
        return

    with open(output_file, "wb") as f:
        f.write(decrypted)

    print(f"[✓] File '{input_file}' decrypted and saved as '{output_file}'")

# --- Menu ---
def main():
    print("\n=== File Encryption/Decryption Tool ===")
    print("1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        generate_key()
    elif choice == '2':
        infile = input("Enter path of file to encrypt: ")
        outfile = input("Enter output filename (e.g., encrypted.txt): ")
        encrypt_file(infile, outfile)
    elif choice == '3':
        infile = input("Enter path of file to decrypt: ")
        outfile = input("Enter output filename (e.g., decrypted.txt): ")
        decrypt_file(infile, outfile)
    elif choice == '4':
        print("Exiting.")
    else:
        print("[!] Invalid option.")

if __name__ == "__main__":
    main()
