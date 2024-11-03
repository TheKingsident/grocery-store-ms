import csv
import os

def load_user_data(user_file):
    """
    Load user data from a CSV file.
    This function reads user data from a specified CSV file and returns a list of user dictionaries.
    Each dictionary contains user information with keys 'username' and 'password'.
    Args:
        user_file (str): The path to the CSV file containing user data.
    Returns:
        list: A list of dictionaries, where each dictionary represents a user with 'username' and 'password' keys.
              If the file does not exist or an error occurs, an empty list is returned.
    Raises:
        OSError: If there is an issue opening the file.
        Exception: If an unexpected error occurs during file reading.
    """
    users = []
    
    # Check if the file exists
    if not os.path.isfile(user_file):
        print(f"Error: The file '{user_file}' does not exist.")
        return users  # Return an empty list if the file is not found
    
    try:
        with open(user_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Optionally validate that the necessary fields exist
                if 'username' in row and 'password' in row:
                    users.append(row)
                else:
                    print("Warning: Missing 'username' or 'password' in row:", row)
    except OSError as e:
        print(f"Error: Unable to open file '{user_file}'. Reason: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return users
