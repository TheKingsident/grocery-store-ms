import csv


def load_grocery_data(grocery_file):
    """
    Loads grocery data from a CSV file into a dictionary.
    Args:
        grocery_file (str): The path to the CSV file containing grocery data.
    Returns:
        dict: A dictionary where each key is a grocery ID and each value is
            another dictionary containing the grocery's name, price, and stock.
    The CSV file is expected to have the following columns:
        - id: The unique identifier for the grocery item.
        - name: The name of the grocery item.
        - price: The price of the grocery item.
        - stock: The stock quantity of the grocery item.
    Example:
        grocery_data = load_grocery_data('groceries.csv')
    """
    grocery_data = {}
    with open(grocery_file, mode='r') as file:
        reader = csv.DictReader(file)
        reader.fieldnames = [field.strip() for field in reader.fieldnames]
        for row in reader:
            grocery_id = row['id'].strip()
            grocery_data[grocery_id] = {
                'name': row['name'],
                'price': float(row['price']),
                'stock': int(row['stock'])
            }
    return grocery_data
