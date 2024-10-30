#!/usr/bin/env python3

import sys
import json
from grocery_load import load_grocery_data
from transaction_load import load_transaction_data
from users_load import load_user_data

def authenticate_user(users):
    """
    Authenticates a user by checking the provided username and password against
        a dictionary of users.
    Args:
        users (dict): A dictionary where the keys are usernames and the values
            are passwords.
    Returns:
        bool: True if the username exists in the dictionary and the password
            matches, False otherwise.
    """
    username = input("Username: ")
    password = input("Password: ")
    return users.get(username) == password

def main(grocery_file, transaction_file, user_file):
    grocery_data = load_grocery_data(grocery_file)
    transaction_data = load_transaction_data(transaction_file)
    user_data = load_user_data(user_file)
    # print(json.dumps(user_data, indent=4))
    # print(json.dumps(transaction_data, indent=4))
    # print(json.dumps(grocery_data, indent=4))
    
    if not authenticate_user(user_data):
        print("Authentication failed")
        return


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python grocery_store.py <transaction_file> <grocery_file> <user_file>")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2], sys.argv[3])