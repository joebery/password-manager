# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 18:38:50 2026

@author: joebe
"""

from cryptography.fernet import Fernet


def encrypt(password):
    key = Fernet.generate_key()
    cipher = Fernet(key)
    
    encrypted = cipher.encrypt(password)
    print(encrypted)
    
    decrypted = cipher.decrypt(encrypted)
    print(decrypted)
    return decrypted
    
    
    
print(encrypt(input('enter password').encode()))
