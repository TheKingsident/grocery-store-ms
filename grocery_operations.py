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

def save_grocery_data(grocery_file, grocery_data):
    """
    Saves grocery data to a CSV file.
    Args:
        grocery_file (str): The path to the CSV file to save the grocery data to.
        grocery_data (dict): A dictionary where each key is a grocery ID and each
            value is another dictionary containing the grocery's name, price, and stock.
    The CSV file will have the following columns:
        - id: The unique identifier for the grocery item.
        - name: The name of the grocery item.
        - price: The price of the grocery item.
        - stock: The stock quantity of the grocery item.
    Example:
        grocery_data = {
            '1': {'name': 'Apple', 'price': 0.5, 'stock': 100},
            '2': {'name': 'Banana', 'price': 0.3, 'stock': 200}
        }
        save_grocery_data('groceries.csv', grocery_data)
    """
    with open(grocery_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'name',
                                                  'price', 'stock'])
        writer.writeheader()
        for grocery_id, grocery_info in grocery_data.items():
            writer.writerow({
                'id': grocery_id,
                'name': grocery_info['name'],
                'price': grocery_info['price'],
                'stock': grocery_info['stock']
            })

def add_new_grocery_item(grocery_file, grocery_data):
    new_grocery_id = str(len(grocery_data) + 1)
    name = input("Enter grocery name: ")
    price = float(input("Enter grocery price: "))
    stock = int(input("Enter grocery stock: "))

    grocery_data[new_grocery_id] = {
        'name': name,
        'price': price,
        'stock': stock
    }
    save_grocery_data(grocery_file, grocery_data)
    print("Grocery item added successfully.")

def edit_grocery_item(grocery_file, grocery_data):
    grocery_id = input("Enter grocery ID to edit: ")
    if grocery_id not in grocery_data:
        print("Grocery ID not found.")
        return
    
    print(f"Editing {grocery_data[grocery_id]['name']} with ID {grocery_id}")

    name  = input(f"New name for {grocery_data[grocery_id]['name']}: ") or grocery_data[grocery_id]['name']
    price = input(f"Current price: {grocery_data[grocery_id]['price']}. New price: ") or grocery_data[grocery_id]['price']
    stock = input(f"Current stock: {grocery_data[grocery_id]['stock']}. New stock: ") or grocery_data[grocery_id]['stock']

    grocery_data[grocery_id]["name"] = name
    grocery_data[grocery_id]["price"] = float(price)
    grocery_data[grocery_id]["stock"] = int(stock)

    save_grocery_data(grocery_file, grocery_data)
    print("Grocery item Updated successfully.")
