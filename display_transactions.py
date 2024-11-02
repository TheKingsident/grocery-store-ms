from datetime import datetime
import matplotlib.pyplot as plt

def plot_bar_chart(sorted_sales, product_names):
    """
    Plots a bar chart using the given data.
    Args:
        data (dict): A dictionary where keys are x-axis labels and values are y-axis values.
        title (str): The title of the bar chart.
        xlabel (str): The label for the x-axis.
        ylabel (str): The label for the y-axis.
    """
    sales_values = [value for _, value in sorted_sales]

    fig, ax = plt.subplots()
    ax.bar(product_names, sales_values, color='orange')
    ax.set_title("Total Sales Values by Product")
    ax.set_xlabel("Product")
    ax.set_ylabel("Total Sales Value")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("monthly_sales.png")
    plt.show()

def plot_graph(monthly_sales, title):
    months = sorted(monthly_sales.keys())
    sales_values = [monthly_sales[month]['value'] for month in months]
    sales_counts = [monthly_sales[month]['count'] for month in months]
    sales_quantity = [monthly_sales[month]['stock'] for month in months]

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
    plt.savefig("monthly_sales.png")
    plt.show()

def display_monthly_sales(transactions, start_month, end_month):
    try:
        start_date = datetime.strptime(start_month, "%m/%Y")
        end_date = datetime.strptime(end_month, "%m/%Y")
    except ValueError:
        print("Error: Please use YYYY/MM format for start and end months.")
        return
    
    monthly_sales = {}
    for t in transactions:
        transaction_date = datetime.strptime(t['date'], "%d/%m/%Y")
        if start_date <= transaction_date <= end_date:
            month = transaction_date.strftime("%y-%m")
            if month not in monthly_sales:
                monthly_sales[month] = {'value': 0, 'stock': 0, 'count': 0}
            monthly_sales[month]['value'] += float(t['payment'])
            monthly_sales[month]['stock'] += int(t['quantity'])
            monthly_sales[month]['count'] += 1
    
    grapth_tile = "Monthly Sales Values and Number of Sales"
    plot_graph(monthly_sales, grapth_tile)

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

    # Filter and group transactions by month for the specified product
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

    graph_title = f"Monthly Sales for {groceries[grocery_id]['name']}. Grocery ID: {grocery_id}."
    plot_graph(monthly_sales, graph_title)
