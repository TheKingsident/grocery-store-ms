
import csv

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

    with open(transaction_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file,
                                fieldnames=['date', 'time', 'id', 'payment'])
        writer.writeheader()
        for transaction in transactions:
            writer.writerow(transaction)
