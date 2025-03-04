# Secure Passwords Generator

## Objective  
The **Secure Passwords Generator** project was developed to create strong, randomly generated passwords that enhance security for online accounts, applications, and sensitive data storage. This project aims to help users generate passwords that follow best security practices, reducing the risk of brute-force and dictionary attacks. 

Additionally, this tool allows mass password generation, security strength verification, and secure storage of generated passwords using encryption.

## Features
- **Random Password Generation**: Generates passwords of a customizable length, combining uppercase, lowercase, numbers, and special characters.
- **Password Strength Check**: Evaluates the strength of generated passwords based on their entropy and complexity, providing feedback on their security level (Weak, Medium, or Strong).
- **Mass Password Generation**: Allows the generation of multiple passwords in one go for bulk use.
- **Secure Storage**: Saves the generated passwords in an encrypted file to prevent unauthorized access.
- **Exporting Encrypted Passwords**: Provides the ability to export passwords to a secure, encrypted file format (JSON).

## Skills Learned  
- Understanding of cryptographic randomness and password entropy.  
- Implementation of secure password policies (length, complexity, character sets).  
- Proficiency in Python for security-related applications.  
- Handling user input and implementing CLI/GUI interactions.  
- Strengthening cybersecurity awareness in authentication mechanisms.  
- Understanding of encryption and secure file handling using the `cryptography` library.

## Tools Used  
- **Python** – Core language.
- **Random & Secrets Libraries** – Used for secure random password generation.  
- **Cryptography Library** – For encryption and secure storage of passwords.
- **JSON** – For storing passwords in an encrypted file format.

## How to Use
1. Clone the repository or download the script.
2. Run the script in your Python environment.
3. Input the desired password length and the number of passwords you want to generate.
4. View the generated passwords and their strength rating.
5. The passwords will be securely saved in an encrypted file (`passwords.json`).
6. To view the saved passwords, you will need the decryption key, which is automatically generated and stored in a `secret.key` file.
