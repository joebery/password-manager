# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 16:29:17 2026

@author: joebe
"""
import json 
import sys
import hashlib
from cryptography.fernet import Fernet


class PasswordEntry:  # Class that stores one password entry
    def __init__(self, site_name, user_name, user_password):
        self.site = site_name
        self.username = user_name
        self.password = user_password
        
        
class PasswordManager:
    def __init__(self):
        self.saved_entries = {}  # Dictionary where entries are stored
        
    """########################################################################
                                ENCRYPTION STUFF
    ########################################################################"""
    def cyrpt_key(self):
        try: 
            with open("Fernet.bin" , 'rb') as p:
                self.key = p.read()
                print('key found')
        except FileNotFoundError:
            # print('key not found')
            with open("Fernet.bin", "wb") as f:
                self.key = Fernet.generate_key() # Generating a brand new key 
                # Key = the secret 
                f.write(self.key) # Adds to the file 
        return self.key
        
     
         
    def encrypt(self, password):
        cipher = Fernet(self.key)
 
        encrypted = cipher.encrypt(password)# Encrypting the password 
        return encrypted
    
    def decrypt(self, encrypted):
        cipher = Fernet(self.key)
        decrypted = cipher.decrypt(encrypted)# decrypting the password 
        return decrypted
    
    """########################################################################
                                APPLICATION FUNCTIONS
    ########################################################################"""
    
    
    def is_duplicate(self, site_name):
        if site_name in self.saved_entries:
            return True 
        else: 
            return False
        
    def load(self): #function of loading the dictionary 
        try:
            with open('info.json', 'r') as i: #reading the file 
                self.saved_entries = json.load(i) #this loads the json file into a dict
        except json.JSONDecodeError:
                with open("info.json", "w") as i: #creates the json file 
                    self.saved_entries={} # creates an empty dict 
                
    def save(self):
        
        with open('info.json', 'w') as i: # writing to the json file
            json.dump(self.saved_entries,i) # dump 
            
    def list_all(self):
        for i in self.saved_entries:
            print(i)
                
            
    """########################################################################
                                    USER FUNCTIONS
    ########################################################################"""
        
    
    def add(self, entry_object):  # entry_object is whatever gets passed into this method
        self.saved_entries[entry_object.site] = {
            'username': entry_object.username,
            'password': entry_object.password
        } #this is adding the imputs into the directory 
        # print(entry_object)
        # print(type(self.saved_entries))
        return entry_object

    def search(self, site_to_find):
        if site_to_find in self.saved_entries: #looking for the site in the dictionary
            print(f'Entry for {site_to_find} Found!')
            details = self.saved_entries[site_to_find]  #prying fields that are not site
            print(f"Username: {details['username']}") #this is how we are accessing the 2 different fields 
            print(f"Password: {details['password']}")
        else:
            print('entry not found')
    
    def delete(self, site_to_delete):
        if site_to_delete in self.saved_entries: 
            del self.saved_entries[site_to_delete]
    
    
def not_empty(field_to_check):
    while True: 
        if field_to_check != '':
            return field_to_check
            break 
        else: 
           field_to_check = input('field cannot be empty, please try again')
           continue
    
def add_entry(manager):
    
        
        site_name = input('please enter the site you want to enter the information for:').capitalize() 
        site_name = not_empty(site_name)           
        if manager.is_duplicate(site_name):
            while True:
                overwrite = input(f'{site_name} found, would you like to overwrite: Y/N').capitalize()
                if overwrite != '':
                    if overwrite == 'N':
                        return
                    elif overwrite == 'Y':
                        break
                    else: 
                        print(f'"{overwrite}" is not an option please try again')
                else: 
                    print('field cannot be empty')
        
      
        user_name = input(f'please enter the username for {site_name} : ')
        user_name = not_empty(user_name)
                
        user_password = input(f'please enter the password for {site_name} : ')
        user_password = not_empty(user_password)
        encrypted_user_password= manager.encrypt(user_password.encode()).decode()
        
        new_entry = PasswordEntry(site_name, user_name, encrypted_user_password)
        manager.add(new_entry)
        manager.save()
    
            
          
        
def menu():
    
    run_menu = 1
    manager = PasswordManager()
    manager.cyrpt_key()
    manager.load()
    while run_menu == 1:  # Loop allows user tow keep using the program
        menu_choice = input('what would you like to do today 1. ADD 2. SEARCH, 3. DELETE, 4.QUIT:, 5.Other ')
    
        if menu_choice == '1':
           add_entry(manager)
        
        
        elif menu_choice == '2':
            site_to_find = input('what site would you like to search for: ').capitalize() 
            manager.search(site_to_find)
    
    
        elif menu_choice == '3':
            site_to_delete = input('what site would you like to delete: ').capitalize() 
            if manager.is_duplicate(site_to_delete): #if true continue to ask user if they want to delete 
                while True:
                    question_delete = input('Are you sure you want to delete, Y/N').capitalize()
                    if question_delete =='Y':  
                        manager.delete(site_to_delete)
                        print(f"The Entry for the site {site_to_delete} has been deleted ")
                        manager.save()
                        break
                    elif question_delete == 'N':
                        break
                    else: 
                        print(f'{question_delete} is not an option, please try again')
            else:
                print(f'{site_to_delete} does not exist')
                
                
        elif menu_choice == '4':
            sys.exit()
            
        elif menu_choice == '5':
            other_menu = input('1. List all sites, 2. Change master password')
            if other_menu == '1':    
                manager.list_all()
                
            elif other_menu =='2':
                change_password()
            
def change_password(): 
        old_pass = input('What is the old password: ')
        old_pass = hash_da_pass(old_pass)
        with open('master_pass.txt', 'r') as i:
            if old_pass == i.read():
                new_pass = input('What is the new password: ')
                ver_new_pass = input('Enter the new password again: ')
                if new_pass == ver_new_pass:
                    with open("master_pass.txt", "w") as i: #creates the json file
                        i.write(hash_da_pass(new_pass))
                        print('password changed sucsessfully')
                else: print('Passwords dont match')
            else: print('wrong password')
                


def auth():    
    try:
        with open('master_pass.txt', 'r') as i: #reading the file 
            read_pass = i.read()
            rate_limit = 2
            master_pass = input('Enter Master-Password:')
            while rate_limit > 0:
                # master_pass = input(f'Enter Master-Password, You have {rate_limit} trys left: ')
                if read_pass == hash_da_pass(master_pass):
                    menu()
                    return
                master_pass = input(f'Enter Master-Password, You have {rate_limit} trys left: ')

                rate_limit -= 1
            print('Too many failled attempts, Goodbye!')
            sys.exit()
                    
    except FileNotFoundError :
        master_pass = input('You Have Not set a password, please set one now')
        hashed_pass = hash_da_pass(master_pass)
        with open("master_pass.txt", "w") as i: #creates the json file
            i.write(hashed_pass)
            menu()
            
def hash_da_pass(password):
    return hashlib.sha3_256(password.encode()).hexdigest()


    
"""###########################################################################
                                    MAIN
###########################################################################"""
# manager = PasswordManager()r
# manager.load()
      
auth()

        
