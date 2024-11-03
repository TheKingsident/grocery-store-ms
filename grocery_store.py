#!/usr/bin/env python3

import sys
import json
from utils.display_transactions import display_monthly_sales, display_product_sales, display_total_sales
from utils.grocery_operations import load_grocery_data, edit_grocery_item, add_new_grocery_item
from utils.search_transanctions import search_by_date, search_by_name, search_by_name_and_date
from utils.transaction_operations import load_transaction_data, record_sales_transaction
from utils.users_load import load_user_data


def authenticate_user(users):
    """
    Authenticates a user by checking the provided username and password against
        a dictionary of users.
    Args:
        users (list of dict): A list of user dictionaries where each dictionary
            contains 'username', 'password', and 'type'.
    Returns:
        tuple: (bool, username, user_type) where:
            - bool: True if the username exists and the password matches, False otherwise.
            - username: The authenticated username if successful, else None.
            - user_type: The user's type if authentication is successful, else None.
    """
    try:
        if not isinstance(users, list):
            raise ValueError("\nUsers data should be a list of dictionaries.")

        username = input("Username: ").strip()
        password = input("Password: ").strip()

        if not username or not password:
            print("\nError: Username and password cannot be empty.")
            return False, None, None

        user = next((user for user in users if user.get('username') == username), None)

        if user is None:
            print("\nError: Username not found.")
            return False, None, None
        
        if 'password' not in user or 'type' not in user:
            print("\nError: User data is missing required fields.")
            return False, None, None

        if user['password'] == password:
            return True, username, user['type']
        else:
            print("\nError: Incorrect password.")
            return False, None, None

    except ValueError as ve:
        print(f"\nData Error: {ve}")
        return False, None, None

    except Exception as e:
        print(f"Unexpected error: {e}")
        return False, None, None

def main(grocery_file, transaction_file, user_file):
    try:
        try:
            grocery_data = load_grocery_data(grocery_file)
            transaction_data = load_transaction_data(transaction_file)
            user_data = load_user_data(user_file)
        except FileNotFoundError as e:
            print(f"Error: {e}. Please check that the file paths are correct.")
            return
        except json.JSONDecodeError:
            print("Error: Failed to parse data. Please check that the files contain valid JSON.")
            return

        authenticated, username, user_type = authenticate_user(user_data)
        if not authenticated:
            print("Authentication failed.")
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
                print("7. Display monthly sales")
                print("8. Display grocery sales")
                print("9. Display total sales")
                print("10. Exit\n")
                choice = input("Select an option: ")

                try:
                    if choice == '1':
                        record_sales_transaction(grocery_data, transaction_file, grocery_file)
                    elif choice == '2':
                        add_new_grocery_item(grocery_file, grocery_data)
                    elif choice == '3':
                        edit_grocery_item(grocery_file, grocery_data)
                    elif choice == '4':
                        search_date = input("\nEnter date (dd/mm/yyyy): ")
                        search_by_date(transaction_data, search_date)
                    elif choice == "5":
                        search_name = input("\nEnter grocery name: ")
                        search_by_name(transaction_data, grocery_data, search_name)
                    elif choice == "6":
                        search_name = input("\nEnter product name: ")
                        start_date = input("Enter start date (dd/mm/yyyy): ")
                        end_date = input("Enter end date (dd/mm/yyyy): ")
                        search_by_name_and_date(transaction_data, grocery_data, search_name, start_date, end_date)
                    elif choice == "7":
                        start_month = input("\nEnter start month (mm/yyyy): ")
                        end_month = input("Enter end month (mm/yyyy): ")
                        display_monthly_sales(transaction_data, start_month, end_month)
                    elif choice == "8":
                        grocery_id = input("\nEnter grocery ID between 1 - 19: ")
                        start_month = input("Enter start month (mm/yyyy): ")
                        end_month = input("Enter end month (mm/yyyy): ")
                        display_product_sales(transaction_data, grocery_data, grocery_id, start_month, end_month)
                    elif choice == "9":
                        start_date = input("\nEnter start date (dd/mm/yyyy): ")
                        end_date = input("Enter end date (dd/mm/yyyy): ")
                        display_total_sales(transaction_data, grocery_data, start_date, end_date)
                    elif choice == '10':
                        print("\nExiting program")
                        break
                    else:
                        print("\nInvalid selection. Please try again.")
                except ValueError as e:
                    print(f"Invalid input: {e}")
                except Exception as e:
                    print(f"An error occurred: {e}")

            elif user_type == 'cashier':
                print("Menu:")
                print("1. Enter sales transaction")
                print("2. Search transactions by date")
                print("3. Search transactions by product name")
                print("4. Search transactions by product name and date range")
                print("5. Exit\n")
                choice = input("Select an option: ")

                try:
                    if choice == '1':
                        record_sales_transaction(grocery_data, transaction_file, grocery_file)
                    elif choice == '2':
                        search_date = input("\nEnter date (dd/mm/yyyy): ")
                        search_by_date(transaction_data, search_date)
                    elif choice == "3":
                        search_name = input("\nEnter grocery name: ")
                        search_by_name(transaction_data, grocery_data, search_name)
                    elif choice == "4":
                        search_name = input("\nEnter product name: ")
                        start_date = input("Enter start date (dd/mm/yyyy): ")
                        end_date = input("Enter end date (dd/mm/yyyy): ")
                        search_by_name_and_date(transaction_data, grocery_data, search_name, start_date, end_date)
                    elif choice == '5':
                        print("\nExiting program")
                        break
                    else:
                        print("\nInvalid selection. Please try again.")
                except ValueError as e:
                    print(f"Invalid input: {e}")
                except Exception as e:
                    print(f"An error occurred: {e}")

            else:
                print("\nInvalid user type.")
                break
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("\nUsage: python grocery_store.py <transaction_file> <grocery_file> <user_file>")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2], sys.argv[3])