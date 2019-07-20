# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 10:31:45 2019

@author: grace
"""
import random


accounts = {}
usernames = {}

class Account:

    def __init__(self, email, password, username, key_ID):
        self.email = email
        self.password = password
        self.username = username
        self.key_ID = key_ID
        usernames[self.username] = self.email
        self.profile_pic = None
        self.about_me = None
        self.location = None
        self.forum_sign = None
        self.forum_post_count = 0
        self.verified = false


    def _additional_details_ (self, details_list):
    
        if len(details_list) > 0:
            self.profile_pic = details_list[0]
            self.about_me = details_list[1]
            self.location = details_list[2]
            self.forum_sign = details_list[3]

    def upload_user_profile(self):
        

    def increase_post_count(self):
        self.forum_post_count += 1
    
    def verified(self):
        self.verified = true

def decrypt(string):
    return string

def generate_key_ID():
    key = ""
    
    for i in range(6):
        random_char_select = random.randint(0,9)
        if random_char_select <= 4:
            random_int = random.randint(48,57)
            key += (str(chr(random_int)))
        elif random_char_select <= 7:
            random_int = random.randint(65,90)
            key += (str(chr(random_int))) 
        else:
            random_int = random.randint(97,122)
            key += (str(chr(random_int)))
            
    return key
    

def verify_login(email, password):
    
    if accounts.get(email) == None:
        print("Incorrect email or password")
    elif accounts.get(email) == password:
        print("Login successful")
        upload_user_profile()
    else:
        print("Incorrect email or password")



def create_account(input):
    accounts[decrypt(input[0])] = Account(decrypt(input[0]), decrypt(input[1]), generate_key_ID())
    upload_user_profile()
    print("Account successfully created")

def login_account():
    input = retrieve_login_input()
    verify_login(decrypt(input[0]), decrypt(input[1]))

def upload_public_user_details(username):
    details = []
    details[0] = usernames[username].profile_pic 
    details[1] = usernames[username].about_me 
    details[2] = usernames[username].location 
    details[3] = usernames[username].forum_sign 
    details[4] = usernames[username].forum_post_count 
    return details

print(generate_key_ID())

