import csv

def load_user_data(user_file):
    users = []
    with open(user_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            users.append(row)
    return users
