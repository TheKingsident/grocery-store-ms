#!/usr/bin/env python3

import sys
import json
from grocery_operations import load_grocery_data, edit_grocery_item, add_new_grocery_item
from search_transanctions import search_by_date, search_by_name, search_by_name_and_date
from transaction_operations import load_transaction_data, record_sales_transaction
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
    
    print(f"\nWelcome {username}!, you are logged in as a {user_type}.\n")

    while True:
        if user_type == 'manager':
            print("Menu:")
            print("1. Enter sales transaction")
            print("2. Add new grocery item")
            print("3. Edit grocery item")
            print("4. Search transactions by date")
            print("5. Search transactions by product name")
            print("6. Search transactions by product name and date range")
            print("7. Exit\n")
            choice = input("Select an option: ")

            if choice == '1':
                record_sales_transaction(grocery_data, transaction_file, grocery_file)

            elif choice == '2':
                add_new_grocery_item(grocery_file, grocery_data)

            elif choice == '3':
                edit_grocery_item(grocery_file, grocery_data)

            elif choice == '4':
                search_date = input("Enter date (dd/mm/yyyy): ")
                search_by_date(transaction_data, search_date)
            
            elif choice == "5":
                search_name = search_name = input("Enter grocery name: ")
                search_by_name(transaction_data, search_name)

            elif choice == "6":
                search_name = input("Enter product name: ")
                start_date = input("Enter start date (dd/mm/yyyy): ")
                end_date = input("Enter end date (dd/mm/yyyy): ")
                search_by_name_and_date(transaction_data, search_name, start_date, end_date)

            elif choice == '7':
                print("Exiting program")
                break

            else:
                print("Invalid selection. Please try again.")

        elif user_type == 'cashier':
            print("1. Enter sales transaction")
            print("2. Search transactions by date")
            print("3. Search transactions by product name")
            print("4. Search transactions by product name and date range")
            print("5. Exit\n")
            choice = input("Select an option: ")

            if choice == '1':
                record_sales_transaction(grocery_data, transaction_file, grocery_file)
            
            elif choice == '2':
                search_date = input("Enter date (dd/mm/yyyy): ")
                search_by_date(transaction_data, search_date)
            
            elif choice == "3":
                search_name = search_name = input("Enter grocery name: ")
                search_by_name(transaction_data, search_name)

            elif choice == "4":
                search_name = input("Enter product name: ")
                start_date = input("Enter start date (dd/mm/yyyy): ")
                end_date = input("Enter end date (dd/mm/yyyy): ")
                search_by_name_and_date(transaction_data, search_name, start_date, end_date)

            elif choice == '5':
                print("Exiting program")
                break

            else:
                print("Invalid selection. Please try again.")

        else:
            print("Invalid user type.")
            break


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python grocery_store.py <transaction_file> <grocery_file> <user_file>")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2], sys.argv[3])