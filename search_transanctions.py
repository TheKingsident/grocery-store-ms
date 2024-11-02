from datetime import datetime


def display_transactions(transactions):
    """
    Display a list of transactions in a formatted table.
    Parameters:
    transactions (list of dict): A list of dictionaries where each dictionary represents a transaction.
        Each dictionary should have the following keys:
        - 'date' (str): The date of the transaction.
        - 'time' (str): The time of the transaction.
        - 'id' (str): The transaction ID.
        - 'quantity' (str): The quantity of items in the transaction.
        - 'payment' (str): The payment amount for the transaction.
    Returns:
    None
    Prints:
    A formatted table of transactions. If the payment value is not a valid number, an error message is printed.
    If no transactions are provided, a message indicating no matching transactions is printed.
    """

    if not transactions:
        print("\nNo matching transactions found.\n")
        return
    
    print(f"\n\n{'Date':<15} {'Time':<15} {'ID':<10} {'Quantity':<10} {'Payment':<10}")
    print('-' * 61)
    for t in transactions:
        try:
            payment = float(t['payment'])
            print(f"{t['date']:<15} {t['time']:<15} {t['id']:<10} {t['quantity']:<10} {payment:<10.2f}")
        except ValueError:
            print("\nError: Payment value is not a valid number.")
    print('\n')


def search_by_date(transactions, date):
    """
    Searches transactions by date and returns a list of transactions on that date.
    """
    matching_transactions = [
        t for t in transactions if t['date'] == date
    ]
    display_transactions(matching_transactions)

def search_by_name(transactions, groceries, name):
    matching_transactions = [
        t for t in transactions
        if t['id'] in groceries and name.lower() in groceries[t['id']]['name'].lower()
    ]
    display_transactions(matching_transactions)

def search_by_name_and_date(transactions, groceries, name, start_date, end_date):
    try:
        start_date = datetime.strptime(start_date, "%d/%m/%Y")
        end_date = datetime.strptime(end_date, "%d/%m/%Y")
    except ValueError:
        print("\nError: Incorrect date format. Please use DD/MM/YYYY.")
        return

    matching_transactions = []
    for t in transactions:
        try:
            transaction_date = datetime.strptime(t['date'], "%d/%m/%Y")
            if t['id'] in groceries and name.lower() in groceries[t['id']]['name'].lower() and start_date <= transaction_date <= end_date:
                matching_transactions.append(t)
        except ValueError:
            print(f"\nError: Incorrect date format in transaction {t['id']}. Skipping this transaction.")
            continue
    display_transactions(matching_transactions)