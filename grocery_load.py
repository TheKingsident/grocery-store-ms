import csv
import sys


def load_grocery_data(grocery_file):
    grocery_data = []
    with open(grocery_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            grocery_data.append(row)
    return grocery_data