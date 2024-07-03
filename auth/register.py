import json 
import os

def register_user():
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
  if not os.path.exists("users.json"):
    return {}
  with open("users.json", "r") as file:
    try:
      return json.load(file)
    except json.JSONDecodeError:
      return {}
  
def save_user_data(data):
  with open("users.json", "w") as file:
    json.dump(data, file, indent=4)
