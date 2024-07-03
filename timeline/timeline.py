import json
import os
import re
from collections import Counter

def display_timeline():
  """
    Displays the timeline of posts. If the timeline is empty, it shows a message indicating that.
    Also displays trending topics based on the content of the posts.
  """
  posts = load_posts()

  if not posts:
    print("The timeline is empty")
  else: 
    print("\nTimeline:")
    for index, post in enumerate(posts, 1):
      print(f"{index}. {post['username']}: {post['content']} [Likes: {post['likes']}, Dislikes: {post['dislikes']}]")
      for idx, comment in enumerate(post.get('comments', []), 1):
        print(f"[Comments: {idx}. {comment['username']}: {comment['content']}]")
    print("\nTrending Topics: ")
    display_trending_topics(posts)

def create_post(username:str):
  """
    Creates a new post by the user.
    
    Args:
        username (str): The username of the person creating the post.
  """
  new_post_content = input("Enter your new post: ").strip()
  new_post = {"username": username, "content": new_post_content, "likes": 0, "dislikes": 0, "comments": []}
  posts = load_posts()
  posts.append(new_post)
  save_posts(posts)
  print("Post added!")

def load_posts():
  """
  Loads the list of posts from the 'posts.json' file. If the file does not exist or is empty, it returns an empty list.
    
  Returns:
    list: List of posts.
  """
  if not os.path.exists("posts.json"):
    return []
  with open("posts.json", "r") as file:
    try:
      return json.load(file)
    except json.JSONDecodeError:
      return []
  
def save_posts(data:list):
  """
  Saves the list of posts to the 'posts.json' file.
    
  Args:
    data (list): List of posts to save.
  """
  with open("posts.json", "w") as file:
    json.dump(data, file, indent=4)


def like_post(index:int):
  """
  Increments the like count of the specified post.
    
  Args:
    index (int): Index of the post to like.
  """
  posts = load_posts()
  if 0 <= index < len(posts):
    posts[index]["likes"] +=1
    save_posts(posts)
    print("Post liked!")
  else:
    print("Invalid post index.")


def dislike_post(index:int):
  """
  Increments the dislike count of the specified post.
    
  Args:
    index (int): Index of the post to dislike.
  """
  posts = load_posts()
  if  0 <= index < len(posts):
    posts[index]["dislikes"] += 1
    save_posts(posts)
    print("Post disliked!")
  else:
    print("Invalid post index.")

def comment_post(index:int, username:str):
  """
  Adds a comment to the specified post.
    
  Args:
    index (int): Index of the post to comment on.
    username (str): Username of the person commenting.
  """
  posts = load_posts()
  if 0 <= index < len(posts):
    comment_content = input("Enter your comment: ").strip()
    new_comment = {"username": username, "content": comment_content}
    posts[index]["comments"].append(new_comment)
    save_posts(posts)
    print("Commment added!")
  else:
    print("Invalid post index.")

def get_topics(content:str):
  """
  Extracts topics (hashtags) from the content of a post.
    
  Args:
    content (str): Content of the post.
    
  Returns:
    list: List of topics found in the content.
  """
  topics = re.findall(r'#\w+', content)
  # print(f"Extracted topics from post: {topics}")
  return topics

def count_topics(posts:list):
  """
  Counts the occurrences of each topic (hashtag) in the list of posts.
    
  Args:
    posts (list): List of posts.
    
  Returns:
    Counter: Counter object with topic counts.
  """

  topic_counter = Counter()
  for post in posts:
    topics = get_topics(post['content'])
    topic_counter.update(topics)
  # print(f"Topic counts: {topic_counter}")
  return topic_counter

def display_trending_topics(posts:list):
  """
  Displays the trending topics based on the content of the posts.
  A topic is considered trending if it appears 5 or more times.
    
  Args:
    posts (list): List of posts.
  """
  topic_counter = count_topics(posts)
  trending_topics = [topic for topic, count in topic_counter.items() if count >= 5]
  if trending_topics:
    for topic in trending_topics:
      print(f"{topic}: {topic_counter[topic]} times")
  else: 
    print("No trending topics.")
