import json
import os

def login_user():
  """
  Authenticates a user based on the provided username and password.
  """
  username = input("Enter your username: ").strip()
  password = input("Enter your password: ").strip()

  user_data = load_user_data()

  if username in user_data and user_data[username] == password:
    print("Login successful!")
    return username
  else:
    print("Invalid username or password. Please try again.")
    return None
  
def load_user_data():
  """
  Loads the list of users from the 'users.json' file. If the file does not exist or is empty, it returns an empty dictionary.
    
  Returns:
    dict: Dictionary of users.
  """
  if not os.path.exists("users.json"):
    return {}
  with open("users.json", "r") as file:
    try:
      return json.load(file)
    except json.JSONDecodeError:
      return {}
    
  