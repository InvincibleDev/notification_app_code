from getpass import getpass
import hashlib
import os

from datetime import datetime

import uuid

def _hash_password(password, salt):
    return hashlib.pbkdf2_hmac('sha256', password, salt, 100000)

def signup(user_store):
    print("\n Sign Up")

    username = input("Enter Username: ")
    if not username:
        print("Username cannot be empty.")
        return
    
    if user_store.find_user_by_username(username):
        print("Username already exists. Please choose a different username.")
        return
    
    password = getpass("Enter Password: ")
    confirm_password = getpass("Confirm Password: ")

    if password !=  confirm_password:
        print("Passwords do not match. Please try again.")
        return
    
    if len(password) < 6:
        print("Password must be at least 6 characters long.")
        return
    
    salt = os.urandom(16)
    hashed_password = _hash_password(password, salt)

    user = {
        "user_id":uuid.uuid4().hex,
        "username": username,
        "password": hashed_password.hex(),
        "salt": salt.hex(),
        "created_at": datetime.now().isoformat(),
    }

    user_store.add_user(user)
    print("User Registered Successfully!")
    return

def login(users):
    print("\n Login")
    username = input("Enter Username: ")
    if not username:
        print("Username cannot be empty.")
        return
    user = users.find_user_by_username(username)
    if not user:
        print("User not found. Please sign up first.")
        return
    
    password = getpass("Enter Password: ")
    salt = user["salt"]
    hashed_password = _hash_password(password, salt)

    if hashed_password != user['password']:
        print("Incorrect password. Please try again.")
        return None
    
    print("Welcome, {}!".format(username))

    return user

print(__name__)