from datetime import datetime
import matplotlib.pyplot as plt

def plot_bar_chart(sorted_sales, grocery_names):
    """
    Plots a bar chart using the given data.
    Args:
        sorted_sales (list of tuple): A list of tuples where each tuple contains a grocery ID and its total sales value.
        grocery_names (list of str): A list of grocery names corresponding to the sales values.
    """
    try:
        # Check if sorted_sales and grocery_names are not empty
        if not sorted_sales or not grocery_names:
            raise ValueError("\nError: No sales data available to plot.")

        # Check if the lengths of sorted_sales and grocery_names match
        if len(sorted_sales) != len(grocery_names):
            raise ValueError("\nError: Mismatch between sales data and grocery names.")

        sales_values = [value for _, value in sorted_sales]

        plt.figure(figsize=(10, 6))
        plt.barh(grocery_names, sales_values, color='skyblue')
        plt.xlabel("Total Sales Value")
        plt.title("Total Sales by Product")
        plt.gca().invert_yaxis()  # To display the highest sales at the top

        plt.savefig("total_sales_value.png")
        plt.show()
    
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"An error occurred while plotting the chart: {e}")

def plot_graph(monthly_sales, title, save_name):
    """
    Plots a graph of monthly sales data.

    Args:
        monthly_sales (dict): A dictionary where keys are month names/identifiers
                              and values are dictionaries with 'value', 'count', and 'stock'.
        title (str): The title of the graph.
        save_name (str): The filename to save the plot.

    Returns:
        None
    """
    if not monthly_sales:
        print("Error: No sales data available to plot.")
        return

    months = sorted(monthly_sales.keys())
    
    # Check if all required keys are present
    try:
        sales_values = [monthly_sales[month]['value'] for month in months]
        sales_counts = [monthly_sales[month]['count'] for month in months]
        sales_quantity = [monthly_sales[month]['stock'] for month in months]
    except KeyError as e:
        print(f"Error: Missing data for month: {e}. Please check the monthly sales data structure.")
        return

    # Check if all sales values are numeric
    if not all(isinstance(value, (int, float)) for value in sales_values):
        print("Error: Sales values must be numeric.")
        return

    if not all(isinstance(count, int) for count in sales_counts):
        print("Error: Sales counts must be integers.")
        return

    if not all(isinstance(stock, int) for stock in sales_quantity):
        print("Error: Stock quantities must be integers.")
        return

    try:
        fig, ax = plt.subplots()
        ax.plot(months, sales_values, label="Monthly Sales Value", color='b', marker='o')
        ax.plot(months, sales_counts, label='Number of Sales', color='g', marker='x')
        ax.plot(months, sales_quantity, label="Number of Items Sold", color="r", marker="*")
        ax.set_title(title)
        ax.set_xlabel("Month")
        ax.set_ylabel("Sales Value / Count")
        ax.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(save_name)
        plt.show()
    except Exception as e:
        print(f"Error: An error occurred while plotting the graph: {e}")

def display_monthly_sales(transactions, start_month, end_month):
    """
    Displays the monthly sales for a given range of months.
    This function processes a list of transactions, filters them by the specified
    date range, and calculates the total sales value, stock quantity, and number
    of transactions for each month within the range. It then plots a graph of the
    monthly sales values and the number of sales.
    Args:
        transactions (list): A list of transaction dictionaries. Each dictionary
                             should contain 'date' (str in "dd/mm/yyyy" format),
                             'payment' (float or str), and 'quantity' (int or str).
        start_month (str): The start month in "MM/YYYY" format.
        end_month (str): The end month in "MM/YYYY" format.
    Returns:
        None
    Raises:
        ValueError: If the date format in transactions or the start/end month is invalid.
    Example:
        transactions = [
            {'date': '15/01/2023', 'payment': '100.50', 'quantity': '2'},
            {'date': '20/02/2023', 'payment': '200.00', 'quantity': '3'}
        ]
        display_monthly_sales(transactions, '01/2023', '02/2023')
    """
    try:
        # Convert start and end month strings to datetime objects
        start_date = datetime.strptime(start_month, "%m/%Y")
        end_date = datetime.strptime(end_month, "%m/%Y")
    except ValueError:
        print("Error: Please use MM/YYYY format for start and end months.")
        return

    if not transactions:
        print("No transactions available to display.")
        return

    monthly_sales = {}
    
    for t in transactions:
        try:
            # Extract and convert the transaction date
            transaction_date = datetime.strptime(t['date'], "%d/%m/%Y")
            
            # Check if the transaction date is within the specified range
            if start_date <= transaction_date <= end_date:
                month = transaction_date.strftime("%y-%m")
                
                # Initialize month entry if it doesn't exist
                if month not in monthly_sales:
                    monthly_sales[month] = {'value': 0, 'stock': 0, 'count': 0}

                # Safely get payment and quantity values
                payment = float(t.get('payment', 0))  # Defaults to 0 if 'payment' key is missing
                quantity = int(t.get('quantity', 0))  # Defaults to 0 if 'quantity' key is missing
                
                monthly_sales[month]['value'] += payment
                monthly_sales[month]['stock'] += quantity
                monthly_sales[month]['count'] += 1

        except ValueError:
            print(f"Error: Invalid transaction data found: {t}")
            continue  # Skip this transaction and continue with the next

    if not monthly_sales:
        print("No sales data found for the specified date range.")
        return

    grapth_title = "Monthly Sales Values and Number of Sales"
    save_file_name = f"{start_date.strftime('%Y-%m-%d')}_to_{end_date.strftime('%Y-%m-%d')}_sales"
    plot_graph(monthly_sales, grapth_title, save_file_name)

def display_product_sales(transactions, groceries, grocery_id, start_month, end_month):
    """
    Display and plot the monthly sales data for a specific grocery item within a given date range.
    Args:
        transactions (list): A list of transaction dictionaries. Each dictionary should contain:
            - 'date' (str): The date of the transaction in "dd/mm/yyyy" format.
            - 'id' (int): The grocery item ID.
            - 'payment' (str): The payment amount for the transaction.
            - 'quantity' (str): The quantity of the item sold in the transaction.
        groceries (dict): A dictionary of grocery items where the key is the grocery ID and the value is a dictionary containing:
            - 'name' (str): The name of the grocery item.
        grocery_id (int): The ID of the grocery item to display sales for.
        start_month (str): The start month in "MM/YYYY" format.
        end_month (str): The end month in "MM/YYYY" format.
    Returns:
        None
    Raises:
        ValueError: If the start or end month is not in the correct "MM/YYYY" format.
        KeyError: If a transaction dictionary is missing expected keys.
        TypeError: If there is a type error in the transaction data.
    Notes:
        - The function checks if the grocery_id exists in the groceries dictionary.
        - It parses the start and end months and ensures the start date is before the end date.
        - It processes each transaction to collect monthly sales data for the specified grocery item within the date range.
        - If no sales data is found, it notifies the user.
        - It prepares a filename and plots the graph using the collected sales data.
    """
    # Check if grocery_id exists in groceries
    if grocery_id not in groceries:
        print("Error: Invalid product ID.")
        return

    # Try to parse the start and end dates
    try:
        start_date = datetime.strptime(start_month, "%m/%Y")
        end_date = datetime.strptime(end_month, "%m/%Y")
    except ValueError:
        print("Error: Please use MM/YYYY format for start and end months.")
        return

    # Ensure the start date is before the end date
    if start_date > end_date:
        print("Error: Start date must be before end date.")
        return

    monthly_sales = {}
    
    # Process each transaction
    for t in transactions:
        try:
            transaction_date = datetime.strptime(t['date'], "%d/%m/%Y")
            # Check if the transaction is for the specified grocery_id and within the date range
            if t['id'] == grocery_id and start_date <= transaction_date <= end_date:
                month = transaction_date.strftime("%Y-%m")
                # Initialize monthly sales data if the month is not already present
                if month not in monthly_sales:
                    monthly_sales[month] = {'value': 0, 'stock': 0, 'count': 0}
                # Update the monthly sales data
                monthly_sales[month]['value'] += float(t['payment'])
                monthly_sales[month]['stock'] += int(t['quantity'])
                monthly_sales[month]['count'] += 1
        except ValueError as e:
            print(f"Error processing transaction date '{t['date']}': {e}")
        except KeyError as e:
            print(f"Error: Missing expected key in transaction data: {e}")
        except TypeError as e:
            print(f"Error with transaction data types: {e}")

    # If no sales data is collected, notify the user
    if not monthly_sales:
        print("No sales data found for the specified grocery item in the given date range.")
        return

    # Prepare the filename and plot the graph
    file_start_date = start_date.strftime('%Y-%m-%d')
    file_end_date = end_date.strftime('%Y-%m-%d')

    graph_title = f"Monthly Sales for {groceries[grocery_id]['name']}. Grocery ID: {grocery_id}."
    save_file_name = f"{grocery_id}_{groceries[grocery_id]['name']}_{file_start_date}_to_{file_end_date}_sales"
    plot_graph(monthly_sales, graph_title, save_file_name)

def display_total_sales(transactions, groceries, start_date, end_date):
    """
    Displays a bar chart of total sales by product within a specified date range.
    Args:
        transactions (list of dict): A list of transaction records, where each record is a dictionary
                                     containing 'date' (str in DD/MM/YYYY format), 'id' (str), and 'payment' (str).
        groceries (dict): A dictionary of grocery items where keys are grocery IDs and values are dictionaries
                          containing 'name' (str) and other grocery details.
        start_date (str): The start date of the range in DD/MM/YYYY format.
        end_date (str): The end date of the range in DD/MM/YYYY format.
    Returns:
        None: This function does not return any value. It prints an error message if the date format is incorrect
              and displays a bar chart of total sales by product within the specified date range.
    """
    # Check input types
    if not isinstance(transactions, list) or not isinstance(groceries, dict) or not isinstance(start_date, str) or not isinstance(end_date, str):
        print("Error: Invalid input types. Please check the types of your arguments.")
        return

    try:
        start_date = datetime.strptime(start_date, "%d/%m/%Y")
        end_date = datetime.strptime(end_date, "%d/%m/%Y")
    except ValueError:
        print("\nError: Please use DD/MM/YYYY format for start and end dates.")
        return
    
    grocery_total_sales = {}
    for t in transactions:
        # Validate transaction structure
        if not isinstance(t, dict) or 'date' not in t or 'id' not in t or 'payment' not in t:
            print(f"Skipping invalid transaction: {t}")
            continue

        try:
            transaction_date = datetime.strptime(t['date'], "%d/%m/%Y")
            if start_date <= transaction_date <= end_date:
                grocery_id = t['id']
                
                # Validate grocery ID exists in groceries
                if grocery_id not in groceries:
                    print(f"Warning: Grocery ID {grocery_id} not found in grocery data. Skipping transaction.")
                    continue
                
                # Validate payment data
                payment = t['payment']
                if isinstance(payment, (int, float, str)) and str(payment).replace('.', '', 1).isdigit():
                    grocery_total_sales[grocery_id] = grocery_total_sales.get(grocery_id, 0) + float(payment)
                else:
                    print(f"Skipping transaction {t} due to invalid payment data.")
        except ValueError:
            print(f"Skipping transaction due to invalid date format in transaction {t}")

    # Check if there are any sales to display
    if not grocery_total_sales:
        print("\nNo sales found in the specified date range.")
        return

    sorted_sales = sorted(grocery_total_sales.items(), key=lambda x: x[1], reverse=True)
    grocery_names = [groceries[grocery_id]['name'] for grocery_id, _ in sorted_sales]
    
    # Ensure grocery names match the sales
    if len(grocery_names) != len(sorted_sales):
        print("Warning: Some grocery names could not be found for the sales data.")
    
    plot_bar_chart(sorted_sales, grocery_names)
