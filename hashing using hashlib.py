# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 16:29:17 2026

@author: joebe
"""
import json 
import sys
import time
import hashlib

class PasswordEntry:  # Class that stores one password entry
    def __init__(self, site_name, user_name, user_password):
        self.site = site_name
        self.username = user_name
        self.password = user_password


class PasswordManager:
    def __init__(self):
        self.saved_entries = {}  # Dictionary where entries are stored
        

    def add(self, entry_object):  # entry_object is whatever gets passed into this method
        self.saved_entries[entry_object.site] = {
            'username': entry_object.username,
            'password': entry_object.password
        } #this is adding the imputs into the directory 

        # print(entry_object)
        # print(type(self.saved_entries))
        return entry_object
    
    def is_duplicate(self, site_name):
        if site_name in self.saved_entries:
            return True
        else: 
            return False 

    def search(self, site_to_find):
        if site_to_find in self.saved_entries: #looking for the site in the dictionary
            print(f'Entry for {site_to_find} Found!')
            details = self.saved_entries[site_to_find]  #prying feilds that are not site
            print(f"Username: {details['username']}") #this is how we are accessing the 2 different feilds 
            print(f"Password: {details['password']}")
        else:
            print('entry not found')
    
    def delete(self, site_to_delete):
        while True:
            question_delete = input('Are you sure you want to delete, Y/N').capitalize()
            if question_delete == 'Y':
                if site_to_delete in self.saved_entries: 
                    del self.saved_entries[site_to_delete]
                    print(f"The Entry for the site {site_to_delete} has been deleted ")
                    break
                else:
                    print('entry not found')
            elif question_delete =='N': 
                print('Goodbye')
                break
            else: 
                print('That was not an option Please try again')
                   
    def load(self): #function of loading the dictionary 
        try:
            with open('info.json', 'r') as i: #reading the file 
                self.saved_entries = json.load(i) #this loads the json file into a dict
        except:
                with open("info.json", "w") as i: #creates the json file 
                    self.saved_entries={} # creates an empty dict 
                
    def save(self):
        with open('info.json', 'w') as i: # writing to the json file
            json.dump(self.saved_entries,i) # dump 
            
    def list_all(self):
        for i in self.saved_entries:
            print(i)
        
    
def add_entry(manager):
    
        while True: 
            site_name = input('please enter the site you want to enter the information for:').capitalize() 
            if site_name != '':
                break 
            else: 
                print('Feild cannot be empty')
            
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
                    print('feild cannot be empty')
        
        while True: 
            user_name = input(f'please enter the username for {site_name} : ')
            if user_name != '':
                break 
            else: 
                print('Feild cannot be empty')
                
        while True: 
            user_password = input(f'please enter the password for {site_name} : ')
            if user_password != '':
                break 
            else: 
                print('Feild cannot be empty')
        
        new_entry = PasswordEntry(site_name, user_name, user_password)
        manager.add(new_entry)
        manager.save()
    
            
          
        
def menu():
    run_menu = 1
    manager = PasswordManager()
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
            manager.delete(site_to_delete)
            manager.save()
    
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
                        menu()
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
    
             

    

# manager = PasswordManager()
# manager.load()
        
auth()
        
