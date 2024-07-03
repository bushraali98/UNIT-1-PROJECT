# CLI Social Media Project

## Overview

This project is a command-line interface (CLI) social media application where users can create an account, log in, write posts, like and dislike posts, comment on posts, and view trending topics. The project is designed to be interactive on the CLI.

## Features

### User Account Management
- **Register**: Users can create an account with a unique username and a password (minimum 8 characters).
- **Login**: Registered users can log in using their username and password.
- **Logout**: Users can log out of their account.

### Timeline
- **View Timeline**: Users can view the timeline which displays all posts along with the username of the author, likes, dislikes, and comments.
- **Write Post**: Users can write new posts.
- **Like/Dislike Post**: Users can like or dislike posts.
- **Comment on Post**: Users can comment on posts.
- **Trending Topics**: Displays trending topics based on hashtags used in posts. Topics mentioned 5 or more times are considered trending.

## Usage

### Running the Project

To run the project, navigate to the project directory and execute the following command:

```sh
python run.py
```

### Interacting with the CLI

After starting the application, follow the prompts to interact with the social media application. Here are the commands you can use:

#### Account Management
- **Register**: If you don't have an account, you will be prompted to register by providing a username and a password.
- **Login**: If you have an account, you will be prompted to log in using your username and password.

#### Timeline Interaction
- **View Timeline**: The timeline displays all posts. If there are no posts, it will indicate that the timeline is empty.
- **Write Post**: After logging in, you can write a new post by typing your content when prompted.
- **Like/Dislike Post**: You can like or dislike a post by entering the post number when prompted.
- **Comment on Post**: You can comment on a post by entering the post number and then your comment when prompted.
- **Trending Topics**: Trending topics are displayed based on the frequency of hashtags used in posts.

#### Exiting the Application
- **Logout**: You can log out of your account by typing `logout`.
- **Exit**: You can exit the application by typing `exit`.

## Example Interaction

1. **Starting the Application**:
   ```sh
   Welcome to the CLI Project!
   Do you have an account? (yes/no): no
   ```

2. **Registering a New User**:
   ```sh
   Create a username: user1
   Create a password (min 8 characters): password123
   Account created! Please log in.
   ```

3. **Logging In**:
   ```sh
   Username: user1
   Password: password123
   Login successful!
   ```

4. **Writing a Post**:
   ```sh
   Do you want to write a new post, like a post, dislike a post, comment on a post, logout, or exit? (post/like/dislike/comment/logout/exit): post
   Enter your new post: Hello World! #python
   Post added!
   ```

5. **Viewing Timeline and Trending Topics**:
   ```sh
   Timeline:
   1. user1: Hello World! #python [Likes: 0, Dislikes: 0]
   
   Trending Topics:
   No trending topics.
   ```

6. **Liking a Post**:
   ```sh
   Do you want to write a new post, like a post, dislike a post, comment on a post, logout, or exit? (post/like/dislike/comment/logout/exit): like
   Enter the post number to like: 1
   Post liked!
   ```

7. **Commenting on a Post**:
   ```sh
   Do you want to write a new post, like a post, dislike a post, comment on a post, logout, or exit? (post/like/dislike/comment/logout/exit): comment
   Enter the post number to comment on: 1
   Enter your comment: Great post!
   Comment added!
   ```

8. **Logging Out and Exiting**:
   ```sh
   Do you want to write a new post, like a post, dislike a post, comment on a post, logout, or exit? (post/like/dislike/comment/logout/exit): logout
   Logged out successfully.
   Welcome to the CLI Project!
   Do you have an account? (yes/no): exit
   Goodbye!
   ```

## Project Structure

The project is organized into the following modules and packages:

- **auth**: Contains `register.py` and `login.py` for user registration and login functionalities.
- **timeline**: Contains `timeline.py` for managing and displaying the timeline, posts, likes, dislikes, comments, and trending topics.
- **run.py**: The main entry point to start the application.
- **main.py**: Contains the main logic for interacting with the user and navigating between different functionalities.

By following these steps and using the provided commands, you can interact with the CLI social media application and explore its features.
