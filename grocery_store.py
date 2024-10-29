#!/usr/bin/env python3

import sys
import json
from grocery_load import load_grocery_data
from transaction_load import load_transaction_data

def main(grocery_file, transaction_file):
    grocery_data = load_grocery_data(grocery_file)
    transaction_data = load_transaction_data(transaction_file)
    print(json.dumps(transaction_data, indent=4))
    # print(json.dumps(grocery_data, indent=4))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python grocery_store.py <transaction_file> <grocery_file>")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])