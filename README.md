# Password Manager

A command-line password manager built in Python.

![Python](https://img.shields.io/badge/language-Python-blue.svg)

## 🎯 What This Project Does
This project is a terminal-based password manager that allows users to securely store and manage their passwords. It includes features such as master password protection, encrypted storage, and a user-friendly interface.

## 🛠️ Tech Stack
| Technology         | Description                                         |
|--------------------|-----------------------------------------------------|
| Python             | Programming language used for development           |
| hashlib            | Library for hashing passwords                        |
| cryptography       | Library for encrypting stored passwords              |
| JSON               | Format used for storing data                        |

## 🌟 Features
- 🔒 **Master password protection** — hashed using SHA3-256, plain text password is never stored.
- 🚫 **Rate limiting** — locks out the user after too many failed attempts.
- 🛠️ **First time setup** — prompts for master password on first run.
- ➕ **Add entries** — store site name, username, and password.
- ⚠️ **Duplicate detection** — warns if a site exists before overwriting.
- 🔍 **Search entries** — look up stored entries by site name.
- 🗑️ **Delete entries** — remove an entry with confirmation.
- 📜 **List all sites** — view all saved site names at a glance.
- 💾 **Persistent storage** — entries saved to `info.json` using JSON format.
- ✅ **Input validation** — rejects empty fields.

## 🚀 Getting Started
### Prerequisites
- Make sure Python 3 is installed.

### Installation Steps
1. Clone or download the repository.
2. Run the main file:
   ```bash
   python "hashing using hashlib.py"
   ```
3. On first run, you will be prompted to set a master password.
4. Use the menu to manage your passwords.

## 📅 What Changed In This Update
- Implemented a password generator for creating strong passwords.
- Added decryption capabilities to improve security.
- Updated README to reflect the recent changes in password encryption.

## 🏗️ Architecture
```
+---------------------+
|  Password Manager   |
+---------------------+
|  ├── hashing using   |
|  |   hashlib.py      |
|  ├── info.json      |
|  ├── master_pass.txt |
|  └── Fernet.bin     |
+---------------------+
```

## 🤝 Contributing
Contributions are welcome! Please open an issue or submit a pull request with your proposed changes.

## 📄 License
This project is licensed under the MIT License. Please see the LICENSE file for details.