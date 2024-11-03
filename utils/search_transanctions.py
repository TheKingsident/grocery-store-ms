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

    for i, t in enumerate(transactions):
        try:
            # Check for missing keys
            required_keys = ['date', 'time', 'id', 'quantity', 'payment']
            for key in required_keys:
                if key not in t:
                    raise KeyError(f"Transaction {i + 1} is missing the key '{key}'.")

            # Check types of specific fields
            if not isinstance(t['quantity'], (int, str)) or not isinstance(t['payment'], (float, int, str)):
                raise TypeError(f"Transaction {i + 1} has invalid types for 'quantity' or 'payment'.")
            
            # Convert payment to float for formatting
            payment = float(t['payment'])
            print(f"{t['date']:<15} {t['time']:<15} {t['id']:<10} {t['quantity']:<10} {payment:<10.2f}")
        
        except KeyError as e:
            print(f"\nError: {e}. Transaction skipped.")
        
        except ValueError:
            print(f"\nError: Payment value '{t.get('payment')}' in transaction {i + 1} is not a valid number.")
        
        except TypeError as e:
            print(f"\nError: {e}. Transaction skipped.")
    
    print('\n')



def search_by_date(transactions, date):
    """
    Searches transactions by date and returns a list of transactions on that date.
    Args:
        transactions (list of dict): List of transaction records.
        date (str): The date to search for in 'dd/mm/yyyy' format.
    """
    try:
        datetime.strptime(date, "%d/%m/%Y")

        matching_transactions = [
            t for t in transactions if t.get('date') == date
        ]

        if matching_transactions:
            display_transactions(matching_transactions)
        else:
            print(f"\nNo transactions found for the date: {date}")

    except ValueError as ve:
        print(f"\nError: Invalid date format. Please use 'dd/mm/yyyy'. Details: {ve}")

    except KeyError as ke:
        print(f"\nError: Missing expected field in transaction data. Details: {ke}")

    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

def search_by_name(transactions, groceries, name):
    """
    Searches transactions by grocery name and returns a list of matching transactions.
    Args:
        transactions (list of dict): List of transaction records.
        groceries (dict): Dictionary with grocery IDs as keys and grocery info as values.
        name (str): The grocery name or partial name to search for.
    """
    try:
        matching_transactions = [
            t for t in transactions
            if t.get('id') in groceries and name.lower() in groceries[t['id']].get('name', '').lower()
        ]

        if matching_transactions:
            display_transactions(matching_transactions)
        else:
            print(f"\nNo transactions found for grocery name containing: '{name}'")

    except KeyError as ke:
        print(f"\nError: Missing expected field in transaction or grocery data. Details: {ke}")

    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

from datetime import datetime

def search_by_name_and_date(transactions, groceries, name, start_date, end_date):
    """
    Searches transactions by grocery name and date range, and returns a list of matching transactions.
    Args:
        transactions (list of dict): List of transaction records.
        groceries (dict): Dictionary with grocery IDs as keys and grocery info as values.
        name (str): The grocery name or partial name to search for.
        start_date (str): Start date in DD/MM/YYYY format.
        end_date (str): End date in DD/MM/YYYY format.
    """
    try:
        start_date = datetime.strptime(start_date, "%d/%m/%Y")
        end_date = datetime.strptime(end_date, "%d/%m/%Y")
    except ValueError:
        print("\nError: Incorrect date format. Please use DD/MM/YYYY.")
        return

    matching_transactions = []
    for t in transactions:
        try:
            transaction_date = datetime.strptime(t.get('date', ''), "%d/%m/%Y")
            
            if (
                t.get('id') in groceries and
                name.lower() in groceries[t['id']].get('name', '').lower() and
                start_date <= transaction_date <= end_date
            ):
                matching_transactions.append(t)
        
        except ValueError:
            print(f"\nError: Incorrect date format in transaction {t.get('id', 'unknown')}. Skipping this transaction.")
            continue
        except KeyError as ke:
            print(f"\nError: Missing expected field ({ke}) in transaction or grocery data. Skipping transaction {t.get('id', 'unknown')}.")
            continue
        except Exception as e:
            print(f"\nAn unexpected error occurred while processing transaction {t.get('id', 'unknown')}: {e}")
            continue

    if matching_transactions:
        display_transactions(matching_transactions)
    else:
        print(f"\nNo transactions found for grocery name containing '{name}' within the specified date range.")
