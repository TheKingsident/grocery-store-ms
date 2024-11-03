import csv
from datetime import datetime
from utils.grocery_operations import save_grocery_data

def load_transaction_data(transaction_file):
    """
    Loads transaction data from a CSV file.
    Args:
        transaction_file (str): The path to the CSV file containing transaction data.
    Returns:
        list: A list of dictionaries, where each dictionary represents a transaction.
    Raises:
        FileNotFoundError: If the specified file does not exist.
        IOError: If there is an error reading the file.
    """
    transactions = []
    try:
        with open(transaction_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions.append(row)
    except FileNotFoundError:
        print(f"Error: File '{transaction_file}' not found.")
    except IOError as e:
        print(f"Error reading file '{transaction_file}': {e}")
    return transactions

def save_transaction_data(transaction_file, transactions):
    """
    Appends transaction data to a CSV file. If the file is empty, writes the header first.

    Args:
        transaction_file (str): The path to the CSV file where transaction data will be saved.
        transactions (list of dict): A list of dictionaries, each containing transaction data with keys 
                                     'date', 'time', 'id', 'quantity', and 'payment'.

    Raises:
        IOError: If there is an error writing to the file.
    """
    try:
        with open(transaction_file, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['date', 'time', 'id', 'quantity', 'payment'])
            file_empty = file.tell() == 0

            if file_empty:
                writer.writeheader()
            for transaction in transactions:
                writer.writerow(transaction)
    except IOError as e:
        print(f"Error writing to file '{transaction_file}': {e}")

def record_sales_transaction(grocery_data, transaction_file, grocery_file):
    """
    Records a sales transaction for a grocery store.
    This function displays the current grocery items, prompts the user to enter a grocery ID and quantity sold,
    updates the stock, and records the transaction details in the specified files.
    Args:
        grocery_data (dict): A dictionary containing grocery items with their details.
        transaction_file (str): The file path where transaction data will be saved.
        grocery_file (str): The file path where updated grocery data will be saved.
    Raises:
        ValueError: If the input for quantity is not a valid integer.
        KeyError: If a required key is missing in the grocery data.
        Exception: For any other unexpected errors.
    """
    print(f"\n{'ID':<10} {'Name':<20} {'Price':<10} {'Stock':<10}")
    print('-' * 50)
    for grocery_id, grocery_info in grocery_data.items():
        print(f"{grocery_id:<10} {grocery_info['name']:<20} {grocery_info['price']:<10.2f} {grocery_info['stock']:<10}")
    print("\n")

    try:
        grocery_id = input("Enter grocery ID: ")
        if grocery_id not in grocery_data:
            print("Error: Grocery ID not found.")
            return

        quantity = int(input("Enter quantity sold: "))
        if grocery_data[grocery_id]['stock'] < quantity:
            print("Error: Insufficient stock.")
            return

        datetime_now = datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
        transaction_data = {
            'date': datetime_now.split()[0],
            'time': datetime_now.split()[1] + ' ' + datetime_now.split()[2],
            'id': grocery_id,
            'quantity': quantity,
            'payment': quantity * round(grocery_data[grocery_id]['price'], 2)
        }
        
        grocery_data[grocery_id]['stock'] -= quantity
        save_transaction_data(transaction_file, [transaction_data])
        save_grocery_data(grocery_file, grocery_data)
        print("Transaction recorded successfully.\n")
        
    except ValueError:
        print("\nError: Invalid input for quantity. Please enter a valid integer.")
    except KeyError as e:
        print(f"\nData error: Missing key {e} in grocery data.")
    except Exception as e:
        print(f"\nUnexpected error occurred: {e}")
