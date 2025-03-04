import string
import random
import os
from cryptography.fernet import Fernet
import json

# Generate key for encryption
def generate_key():
    return Fernet.generate_key()

# Save key to a file for later use
def save_key(key):
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load key from the file
def load_key():
    return open("secret.key", "rb").read()

# Function to check the strength of the password
def check_password_strength(password):
    entropy = 0
    if len(password) >= 12:
        entropy += 10
    if any(char.isdigit() for char in password):
        entropy += 5
    if any(char.islower() for char in password) and any(char.isupper() for char in password):
        entropy += 5
    if any(char in string.punctuation for char in password):
        entropy += 5
    
    if entropy >= 20:
        return "Strong"
    elif entropy >= 10:
        return "Medium"
    else:
        return "Weak"

# Function to generate passwords
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Function to save passwords securely to a file
def save_passwords_to_file(passwords, key):
    fernet = Fernet(key)
    encrypted_passwords = fernet.encrypt(json.dumps(passwords).encode())
    
    with open("passwords.json", "wb") as file:
        file.write(encrypted_passwords)

# User interface
length = int(input('Enter the length of the password: '))
quantity = int(input('Enter the number of passwords to generate: '))

# Generate passwords
passwords = [generate_password(length) for _ in range(quantity)]

# Display passwords and their strength
for password in passwords:
    print(f"Generated password: {password}")
    print(f"Password strength: {check_password_strength(password)}")

# Generate encryption key (only done once)
if not os.path.exists("secret.key"):
    key = generate_key()
    save_key(key)
else:
    key = load_key()

# Save passwords securely to file
save_passwords_to_file(passwords, key)

print("\nPasswords have been saved securely to passwords.json.")