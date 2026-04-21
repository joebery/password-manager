# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 18:38:50 2026

@author: joebe
"""

from cryptography.fernet import Fernet

def cyrpt(password):
    
    
    
    
    try: 
        with open("Fernet.bin" , 'rb') as p:
            key = p.read()
            print('d')
    except FileNotFoundError:
        print('o')
        with open("Fernet.bin", "wb") as f:
            key = Fernet.generate_key() # Generating a brand new key 
            # Key = the secret 
            f.write(key) # Adds to the file 

    cipher = Fernet(key) # This creates a Fernet object using the key 
    # Fernet the lock/unlock tool built from the secret 
    # Used to encrypt/decrypt 
    
    # print(type(key))

    encrypted = cipher.encrypt(password) # Encrypting the password 
    print(f"This is the encrypted password: {encrypted}")
    
    decrypted = cipher.decrypt(encrypted) # Decrypting
    print(f"This is the decrypted password: {decrypted}") #####THIS IS WHAT WE WANT TO STORE IN THE JSON FILE#####
    return decrypted
    
    
    
cyrpt(input('enter password: ').encode()) # Encode since Fernet takes only bytes
