#!/usr/bin/env python3

from datetime import datetime
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

    user = next((user for user in users if user['username'] == username), None)

    if user and user['password'] == password:
        return True, username, user['type']
    
    return False, None, None

def main(grocery_file, transaction_file, user_file):
    grocery_data = load_grocery_data(grocery_file)
    transaction_data = load_transaction_data(transaction_file)
    user_data = load_user_data(user_file)
    # print(json.dumps(user_data, indent=4))
    # print(json.dumps(transaction_data, indent=4))
    # print(json.dumps(grocery_data, indent=4))
    
    authemticated, username, user_type = authenticate_user(user_data)

    if not authemticated:
        print("Authentication failed")
        return
    
    print(f"Welcome {username}!, you are logged in as a {user_type}.")

    while True:
        if user_type == 'manager':
            print("1. Enter sales transaction")
            print("2. Add new grocery item")
            print("3. Logout")
            choice = input("slect an option: ")

            if choice == '1':
                grocery_id = input("Enter grocery ID: ")
                quantity = int(input("Enter quantity sold: "))
                payment = float(input("Enter payment received: "))

                if grocery_id in grocery_data and grocery_data[grocery_id]['stock'] >= quantity:
                    datetime_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    transaction_data.append({
                        'date': datetime_now.split()[0],
                        'time': datetime_now.split()[1],
                        'id': grocery_id,
                        'quantity': quantity,
                        'payment': payment
                    })
                    grocery_data[grocery_id]['stock'] -= quantity
                    print("Transaction recorded successfully.")
                else:
                    print("Invalid grocery ID or insufficient stock.")
            elif choice == '2':
                new_grocery_id = str(len(grocery_data) + 1)
                name = input("Enter grocery name: ")
                price = float(input("Enter grocery price: "))
                stock = int(input("Enter grocery stock: "))

                grocery_data[new_grocery_id] = {
                    'name': name,
                    'price': price,
                    'stock': stock
                }
                print("Grocery item added successfully.")
            elif choice == '3':
                break


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python grocery_store.py <transaction_file> <grocery_file> <user_file>")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2], sys.argv[3])