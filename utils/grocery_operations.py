import csv

def load_grocery_data(grocery_file):
    """
    Loads grocery data from a CSV file into a dictionary.
    Args:
        grocery_file (str): The path to the CSV file containing grocery data.
    Returns:
        dict: A dictionary where each key is a grocery ID and each value is another dictionary 
              containing 'name', 'price', and 'stock' of the grocery item. Returns an empty 
              dictionary if the file is not found or if there are errors in the data.
    Raises:
        FileNotFoundError: If the specified file does not exist.
        IOError: If there is an error reading the file.
        ValueError: If there is an error converting 'price' or 'stock' to their respective types.
    Notes:
        - The CSV file must have 'id', 'name', 'price', and 'stock' as field names.
        - Leading and trailing spaces in field names and values are stripped.
        - If no field names are found in the CSV file, an error message is printed and an empty 
          dictionary is returned.
        - If there is a data error in a row (e.g., non-numeric 'price' or 'stock'), an error 
          message is printed for that row, and the row is skipped.
    """
    grocery_data = {}
    try:
        with open(grocery_file, mode='r') as file:
            reader = csv.DictReader(file)
            if reader.fieldnames is None:
                print("Error: No field names found in CSV file.")
                return {}
            reader.fieldnames = [field.strip() for field in reader.fieldnames]
            for row in reader:
                grocery_id = row['id'].strip()
                try:
                    grocery_data[grocery_id] = {
                        'name': row['name'],
                        'price': float(row['price']),
                        'stock': int(row['stock'])
                    }
                except ValueError as e:
                    print(f"Data error in row {row}: {e}")
    except FileNotFoundError:
        print(f"Error: File '{grocery_file}' not found.")
    except IOError as e:
        print(f"Error reading file '{grocery_file}': {e}")
    return grocery_data

def save_grocery_data(grocery_file, grocery_data):
    """
    Save grocery data to a CSV file.
    Args:
        grocery_file (str): The path to the CSV file where the grocery data will be saved.
        grocery_data (dict): A dictionary containing grocery data. The keys are grocery IDs, 
                             and the values are dictionaries with keys 'name', 'price', and 'stock'.
    Raises:
        IOError: If there is an error writing to the file.
    """
    try:
        with open(grocery_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'name', 'price', 'stock'])
            writer.writeheader()
            for grocery_id, grocery_info in grocery_data.items():
                writer.writerow({
                    'id': grocery_id,
                    'name': grocery_info['name'],
                    'price': grocery_info['price'],
                    'stock': grocery_info['stock']
                })
    except IOError as e:
        print(f"Error writing to file '{grocery_file}': {e}")

def add_new_grocery_item(grocery_file, grocery_data):
    """
    Adds a new grocery item to the grocery data and saves it to the specified file.
    Parameters:
    grocery_file (str): The path to the file where grocery data is stored.
    grocery_data (dict): The current grocery data, where keys are grocery IDs and values are dictionaries 
                         containing 'name', 'price', and 'stock' of each grocery item.
    Prompts the user to input the name, price, and stock of the new grocery item. The new item is then added 
    to the grocery_data dictionary with a new unique ID and saved to the grocery_file.
    Exceptions:
    ValueError: If the user inputs an invalid value for price or stock.
    Exception: If any other unexpected error occurs during the process.
    Prints:
    Success message if the grocery item is added successfully.
    Error message if an input error or any other unexpected error occurs.
    """
    
    try:
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
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

def edit_grocery_item(grocery_file, grocery_data):
    """
    Edit an existing grocery item in the grocery data.
    This function prompts the user to input the grocery ID they wish to edit.
    If the ID is found, it allows the user to update the name, price, and stock
    of the grocery item. The updated data is then saved back to the grocery file.
    Args:
        grocery_file (str): The path to the file where grocery data is stored.
        grocery_data (dict): A dictionary containing grocery items, where keys are
                             grocery IDs and values are dictionaries with item details.
    Raises:
        ValueError: If the input for price or stock is not a valid number.
        Exception: If any other unexpected error occurs during the process.
    Returns:
        None
    """
    try:
        grocery_id = input("Enter grocery ID to edit: ")
        if grocery_id not in grocery_data:
            print("Grocery ID not found.")
            return

        print(f"Editing {grocery_data[grocery_id]['name']} with ID {grocery_id}")

        name = input(f"New name for {grocery_data[grocery_id]['name']}: ") or grocery_data[grocery_id]['name']
        price = input(f"Current price: {grocery_data[grocery_id]['price']}. New price: ") or grocery_data[grocery_id]['price']
        stock = input(f"Current stock: {grocery_data[grocery_id]['stock']}. New stock: ") or grocery_data[grocery_id]['stock']

        grocery_data[grocery_id]["name"] = name
        grocery_data[grocery_id]["price"] = float(price)
        grocery_data[grocery_id]["stock"] = int(stock)

        save_grocery_data(grocery_file, grocery_data)
        print("Grocery item updated successfully.")
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
