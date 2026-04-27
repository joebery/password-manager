# Password Manager

A command-line password manager built in Python as part of a structured learning journey into software development.

---

## About

This project was built from scratch over several sessions as a practical learning exercise covering core Python concepts including classes, file handling, error handling, dictionaries, and hashing. It is a fully functional terminal-based password manager with a master password, persistent storage, and basic security considerations.

---

## Features

- **Master password protection** — hashed using SHA3-256 via Python's `hashlib` module. The plain text password is never stored.
- **Rate limiting** — locks out the user after too many failed master password attempts
- **First time setup** — prompts the user to create a master password on first run
- **Add entries** — store a site name, username, and password
- **Duplicate detection** — warns if a site already exists and asks before overwriting
- **Search entries** — look up a stored entry by site name
- **Delete entries** — remove an entry with confirmation
- **List all sites** — view all saved site names at a glance
- **Persistent storage** — entries saved to `info.json` using Python's `json` module, loaded automatically on startup
- **Input validation** — empty fields are rejected

---

## How to run

1. Make sure Python 3 is installed
2. Clone or download the repository
3. Run the main file:

```bash
python "hashing using hashlib.py"
```

4. On first run you will be prompted to set a master password
5. Use the menu to manage your passwords

---

## Menu options

```
1. ADD    — add a new site entry
2. SEARCH — search for a site by name
3. DELETE — delete an entry
4. QUIT   — exit the program
5. OTHER  — list all saved sites
```

---

## File structure

```
password-manager/
├── hashing using hashlib.py   # main application file
├── info.json                  # encrypted password store (auto generated)
└── master_pass.txt            # hashed master password (auto generated)
└── README.MD                  # This document
└── Fernet.bin                 # encryption key storage (auto generated)
Experiements/                  # folder for trying out new technologies before adding them into the code
└── #see contents# 
```

---

## Security notes

- The master password is hashed using SHA3-256 and never stored in plain text
- Site passwords are currently stored in encrypted text in `info.json`
- Do not share or commit `info.json` or `master_pass.txt` to a public repository
- Current improvement: encrypt stored passwords using the `cryptography` library

---

## Concepts used

This project was built while learning the following Python concepts:

- Classes and inheritance
- Dictionaries and nested dictionaries
- File handling — reading and writing JSON files
- Error handling with try/except
- Hashing with hashlib
- Functions and separation of concerns
- While loops and input validation
- f-strings and string methods

---

## Planned improvements

- Password generator using the `secrets` module
- Copy password to clipboard using `pyperclip`
- Case insensitive search
- Edit existing entries
- Change master password
- GUI interface

---

## Author

Joe — built as part of a Python learning roadmap targeting a junior software developer role.
