
# Grocery Store Management System

This project is a **Grocery Store Management System** implemented in Python. The system provides basic functionalities for managing grocery items, recording sales transactions, and performing analytical queries. It features authentication for different types of users (manager and cashier) and includes several utilities for data handling, reporting, and user interaction.

---

## Project Structure

Here's an overview of the project files and directories:

```plaintext
grocery-store-ms/
│
├── groceries.csv           # CSV file for storing grocery item data
├── transactions.csv        # CSV file for storing transaction data
├── users.csv               # CSV file for storing user authentication data
├── grocery_store.py        # Main script to run the grocery store management system
│
├── LICENSE                 # License file
├── README.md               # Project documentation (this file)
├── total_sales_value.png   # Example visualization of total sales (output)
├── utils/                  # Directory for utility modules
│   ├── __init__.py         # Makes `utils` a package
│   ├── display_transactions.py # Functions for displaying sales and transaction data
│   ├── grocery_operations.py   # Functions for managing grocery items
│   ├── search_transactions.py  # Functions for searching transactions
│   ├── transaction_operations.py # Functions for handling transactions
│   └── users_load.py       # Functions for loading and managing user data
```

---

## Features

1. **User Authentication**: Users can log in with a username and password. Different users (managers, cashiers) have access to different menus and functionalities.
   
2. **Grocery Item Management**:
   - Add new grocery items.
   - Edit existing grocery items.

3. **Sales Transaction Recording**:
   - Record new sales transactions.
   - Maintain records of transactions with details like date, item, and quantity.

4. **Transaction Search**:
   - Search transactions by date.
   - Search transactions by product name.
   - Search transactions by product name within a date range.

5. **Data Display and Analysis**:
   - Display monthly sales.
   - Display sales by grocery item.
   - Display total sales within a date range.

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/TheKingsident/grocery-store-ms.git
   cd grocery-store-ms
   ```

2. **Install required dependencies**:
   This project does not have specific Python package dependencies beyond the standard library. However, ensure you have Python 3 installed.

---

## Usage

To run the system, execute the `grocery_store.py` script with the necessary data files as arguments:

```bash
python3 grocery_store.py groceries.csv transactions.csv users.csv
```

Upon starting, the program will prompt for user login credentials. Based on the user type (manager or cashier), different options will be available.

---

## Detailed Documentation

### 1. Authentication

The system uses a basic authentication mechanism, where the `users.csv` file stores user credentials. Each user has a `username`, `password`, and `type` (either `manager` or `cashier`).

The `authenticate_user` function in `grocery_store.py` prompts for login and verifies the credentials against the data in `users.csv`.

### 2. Menus and Permissions

Depending on the user type, different menus are presented:

- **Manager Menu**:
  - Enter sales transaction
  - Add new grocery item
  - Edit grocery item
  - Search transactions by date, name, or date range
  - Display monthly sales
  - Display sales by grocery item
  - Display total sales
  - Exit

- **Cashier Menu**:
  - Enter sales transaction
  - Search transactions by date, name, or date range
  - Exit

### 3. Grocery Operations

The `utils/grocery_operations.py` module contains functions to manage grocery items, including:
- **Adding New Items**: `add_new_grocery_item` prompts the user to enter details for a new item and saves it to `groceries.csv`.
- **Editing Items**: `edit_grocery_item` allows managers to modify details of existing items in `groceries.csv`.

### 4. Transaction Operations

The `utils/transaction_operations.py` module provides functions for recording and managing transactions:
- **Recording Transactions**: `record_sales_transaction` allows users to log a new sales transaction, updating `transactions.csv`.
- **Loading Transaction Data**: `load_transaction_data` reads transactions from `transactions.csv`.

### 5. Search Functionality

The `utils/search_transactions.py` module allows users to search for transactions based on different criteria:
- **Search by Date**: `search_by_date` retrieves transactions for a specific date.
- **Search by Product Name**: `search_by_name` retrieves transactions based on a grocery item’s name.
- **Search by Name and Date Range**: `search_by_name_and_date` retrieves transactions for a specific item within a date range.

### 6. Data Display

The `utils/display_transactions.py` module provides functionality to display transaction data in various formats:
- **Display Monthly Sales**: `display_monthly_sales` summarizes sales for each month in a given range.
- **Display Product Sales**: `display_product_sales` shows sales of a specific grocery item over a period.
- **Display Total Sales**: `display_total_sales` computes the total sales in a specified date range.

#### Example Data Display

Here is an example of the data displayed by the system:

![Example Data Display](https://github.com/TheKingsident/grocery-store-ms/blob/main/public/2024-02-01_to_2024-10-01_sales.png)

---

## Error Handling

The program includes error handling to manage potential issues:
- **File Errors**: If a CSV file (e.g., `groceries.csv`, `transactions.csv`, `users.csv`) cannot be found or opened, the program will raise an appropriate error message.
- **Authentication Failure**: If user credentials are incorrect, the system will deny access.
- **Input Validation**: When the user selects a menu option, invalid entries are handled gracefully with messages prompting the user to try again.

### Example Error Handling Code

For example, the `load_user_data` function in `users_load.py` has error handling to manage file-related issues:

```python
def load_user_data(user_file):
    users = []
    try:
        with open(user_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                users.append(row)
    except FileNotFoundError:
        print(f"Error: The file {user_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return users
```

---

## CSV File Structure

### groceries.csv

| id  | name      | price | stock |
|-----|-----------|-------|-------|
| 1   | Apple     | 0.50  | 100   |
| 2   | Banana    | 0.30  | 200   |
| ... | ...       | ...   | ...   |

### transactions.csv

| date       | id      | quantity | payment     |
|------------|---------|----------|-------------|
| 01/01/2024 | 1       | 5        | 2.50        |
| 01/01/2024 | 2       | 10       | 3.00        |
| ...        | ...     | ...      | ...         |

### users.csv

| username | password | type     |
|----------|----------|----------|
| admin    | admin123 | manager  |
| cashier1 | pass456  | cashier  |

---

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure your code follows the existing style and includes appropriate error handling.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

---

## Acknowledgements

Special thanks to all contributors and the Python community for the extensive libraries and resources that made this project possible.

---

## Contact

Project Author: Kingsley Usa (cakemurderer)  
GitHub: [TheKingsident](https://github.com/TheKingsident)  
Email: [softwareengineeringcake@gmail.com](mailto:softwareengineeringcake@gmail.com)
