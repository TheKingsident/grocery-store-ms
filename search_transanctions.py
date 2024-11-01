def display_transactions(transactions):
    if not transactions:
        print("No matching transactions found.")
        return
    
    print(f"{'Date':<15} {'Time':<10} {'ID':<5} {'Quantity':<10} {'Payment':<10}")
    print('-' * 50)
    for t in transactions:
        print(f"{t['date']:<15} {t['time']:<10} {t['id']:<5} {t['quantity']:<10} {t['payment']:<10.2f}")


def search_by_date(transactions, date):
    """
    Searches transactions by date and returns a list of transactions on that date.
    """
    matching_transactions = [
        t for t in transactions if t['date'] == date
    ]
    display_transactions(matching_transactions)

def search_by_name(transactions, name):
    matching_transactions = [
        t for t in transactions if name.lower() in transactions['name'].lower()
    ]
    display_transactions(matching_transactions)

