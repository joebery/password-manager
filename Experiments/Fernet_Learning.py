# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 18:38:50 2026

@author: joebe
"""

from cryptography.fernet import Fernet

def cyrpt(password):
    key = Fernet.generate_key() # Generating a brand new key 
    # This needs to be stored in a file, we will use salt.bin 
    # Key = the secret 
    #####THIS WILL BE STORED IN THE SALT.BIN####
    
    
    cipher = Fernet(key) # This creates a Fernet object using the key 
    # Fernet the lock/unlock tool built from the secret 
    # Used to encrypt/decrypt 
    
    
    
    
    encrypted = cipher.encrypt(password) # Encrypting the password 
    print(encrypted)
    
    decrypted = cipher.decrypt(encrypted) # Decrypting
    print(decrypted) #####THIS IS WHAT WE WANT TO STORE IN THE JSON FILE#####
    return decrypted
    
    
    
cyrpt(input('enter password: ').encode()) # Encode since Fernet takes only bytes
