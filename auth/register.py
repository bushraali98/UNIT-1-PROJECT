import json 
import os

def register_user():
  """
  Registers a new user by creating a username and password.
  The password must be at least 8 characters long.
  The username must be unique.
  """
  username = input("Enter a username: ").strip()
  password = input("Eneter a password (at least 8 characters): ").strip()

  if len(password) < 8:
    print("Password must be at least 8 characters long. ")
    return
  
  user_data = load_user_data()
  if username in user_data:
    print("Username already taken. Please try again. ")
    return
  
  user_data[username] = password
  save_user_data(user_data)
  print("Registration successful!")

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
  
def save_user_data(data:dict):
  """
  Saves the list of users to the 'users.json' file.
    
  Args:
    users (dict): Dictionary of users to save.
  """
  with open("users.json", "w") as file:
    json.dump(data, file, indent=4)
