
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
