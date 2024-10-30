
import csv
from datetime import datetime
from grocery_operations import save_grocery_data

def load_transaction_data(transaction_file):
    """
    Loads transaction data from a CSV file.
    Args:
        transaction_file (str): The path to the CSV file containing
            transaction data.
    Returns:
        list[dict]: A list of dictionaries where each dictionary represents a
            transaction.
    """
    transactions = []
    with open(transaction_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            transactions.append(row)
    return transactions

def save_transaction_data(transaction_file, transactions):
    """
    Saves transaction data to a specified CSV file.
    Args:
        transaction_file (str): The path to the CSV file where transaction
            data will be saved.
        transactions (list of dict): A list of dictionaries, each representing
            a transaction. 
            Each dictionary should have the keys 'date', 'time', 'id', and 'payment'.
    Writes:
        A CSV file with the transaction data, including a header row with the field names.
    """

    with open(transaction_file, mode='a', newline='') as file:
        writer = csv.DictWriter(file,
                                fieldnames=['date', 'time', 'id', 'quantity', 'payment'])
        file_empty = file.tell() == 0

        if file_empty:
            writer.writeheader()
        for transaction in transactions:
            writer.writerow(transaction)

def record_sales_transaction(grocery_data, transaction_file, grocery_file):
    grocery_id = input("Enter grocery ID: ")
    quantity = int(input("Enter quantity sold: "))

    if grocery_id in grocery_data and grocery_data[grocery_id]['stock'] >= quantity:
        datetime_now = datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
        transaction_data = {
            'date': datetime_now.split()[0],
            'time': datetime_now.split()[1] +' '+ datetime_now.split()[2],
            'id': grocery_id,
            'quantity': quantity,
            'payment': quantity * round(grocery_data[grocery_id]['price'], 2)
        }
        grocery_data[grocery_id]['stock'] -= quantity
        save_transaction_data(transaction_file, [transaction_data])
        save_grocery_data(grocery_file, grocery_data)
        print("Transaction recorded successfully.")
    else:
        print("Invalid grocery ID or insufficient stock.")
