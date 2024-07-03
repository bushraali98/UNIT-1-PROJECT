from auth.login import login_user
from auth.register import register_user
from timeline.timeline import display_timeline, create_post, like_post, dislike_post, comment_post

def main():
  """
  The main function of the program that handles user registration, login, and various actions like posting,
  liking, disliking, commenting, and logging out.
  """
  print("Welcome to our Socila Media CLI Application")

  while True:
    has_account = input("Do you have an account? (yes/no): ").strip().lower()
    if has_account == "yes":
      username = login_user()
      if username:
        break
    elif has_account == "no":
      register_user()
      print("Account created! Please log in.")
    else:
      print("Invalid input, plese type 'yes' or 'no'. ")

  while True:
    display_timeline()
    action = input("Do you want to write a new post, like a post, dislike a post, comment on a post, logout, or exit? (post/like/dislike/comment/logout/exit): ").strip().lower()
    if action == "post":
      create_post(username)
    elif action == "like":
      index = int(input("Enter the post number to like: ")) - 1
      like_post(index)
    elif action == "dislike":
      index = int((input("Enter the post number to dislike: "))) - 1
      dislike_post(index)
    elif action == "comment":
      index = int(input("Enter the post number to comment on: ")) - 1
      comment_post(index, username)
    elif action == "logout":
      print("Logged out successfully.")
      main() # Restart the process to either log in or register a new account
      break
    elif action == "exit":
      print("Goodbye!")
      break
    else:
      print("Invalid input, please type 'yes', 'no', or 'exit'. ")
