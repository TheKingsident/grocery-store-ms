# Grocery Store Management System

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Introduction

The Grocery Store Management System is a Python-based application designed to manage grocery store operations, including sales transactions, inventory management, and user authentication. The system provides functionalities to record sales, search transactions, display sales data, and manage grocery items.

## Features

- **Sales Transactions**: Record and save sales transactions.
- **Inventory Management**: Add, edit, and load grocery items.
- **User Authentication**: Authenticate users based on a CSV file.
- **Search Transactions**: Search transactions by date, name, or date range.
- **Display Sales Data**: Display total sales, monthly sales, and product-specific sales.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/TheKingsident/grocery-store-ms.git
    cd grocery-store-ms
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Ensure you have the necessary CSV files (`groceries.csv`, `transactions.csv`, `users.csv`) in the project directory.

## Usage

Run the main script with the required arguments:
```sh
python [grocery_store.py](http://_vscodecontentref_/2) <transaction_file> <grocery_file> <user_file>
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.