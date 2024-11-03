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

def display_product_sales(
        transactions,
        groceries,
        grocery_id,
        start_month,
        end_month
    ):
    
    if grocery_id not in groceries:
        print("Error: Invalid product ID.")
        return
    
    try:
        start_date = datetime.strptime(start_month, "%m/%Y")
        end_date = datetime.strptime(end_month, "%m/%Y")
    except ValueError:
        print("Error: Please use YYYY-MM format for start and end months.")
        return

    monthly_sales = {}
    for t in transactions:
        transaction_date = datetime.strptime(t['date'], "%d/%m/%Y")
        if t['id'] == grocery_id and start_date <= transaction_date <= end_date:
            month = transaction_date.strftime("%Y-%m")
            if month not in monthly_sales:
                monthly_sales[month] = {'value': 0, 'stock': 0, 'count': 0}
            monthly_sales[month]['value'] += float(t['payment'])
            monthly_sales[month]['stock'] += int(t['quantity'])
            monthly_sales[month]['count'] += 1

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
    try:
        start_date = datetime.strptime(start_date, "%d/%m/%Y")
        end_date = datetime.strptime(end_date, "%d/%m/%Y")
    except ValueError:
        print("\nError: Please use DD/MM/YYYY format for start and end dates.")
        return
    
    grocery_total_sales = {}
    for t in transactions:
        try:
            transaction_date = datetime.strptime(t['date'], "%d/%m/%Y")
            if start_date <= transaction_date <= end_date:
                grocery_id = t['id']
                grocery_total_sales[grocery_id] =  grocery_total_sales.get(grocery_id, 0) + float(t['payment'])
        except ValueError:
            print(f"Skipping transaction due to invalid date format in transaction {t}")
        except (TypeError, ValueError):
            print(f"Skipping transaction {t} due to invalid payment data.")

    sorted_sales = sorted(grocery_total_sales.items(), key=lambda x: x[1], reverse=True)
    grocery_names = [groceries[grocery_id]['name'] for grocery_id, _ in sorted_sales]
    plot_bar_chart(sorted_sales, grocery_names)
