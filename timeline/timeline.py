import json
import os
import re
from collections import Counter

def display_timeline():
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

def create_post(username):
  new_post_content = input("Enter your new post: ").strip()
  new_post = {"username": username, "content": new_post_content, "likes": 0, "dislikes": 0, "comments": []}
  posts = load_posts()
  posts.append(new_post)
  save_posts(posts)
  print("Post added!")

def load_posts():
  if not os.path.exists("posts.json"):
    return []
  with open("posts.json", "r") as file:
    try:
      return json.load(file)
    except json.JSONDecodeError:
      return []
  
def save_posts(data):
  with open("posts.json", "w") as file:
    json.dump(data, file, indent=4)


def like_post(index):
  posts = load_posts()
  if 0 <= index < len(posts):
    posts[index]["likes"] +=1
    save_posts(posts)
    print("Post liked!")
  else:
    print("Invalid post index.")


def dislike_post(index):
  posts = load_posts()
  if  0 <= index < len(posts):
    posts[index]["dislikes"] += 1
    save_posts(posts)
    print("Post disliked!")
  else:
    print("Invalid post index.")

def comment_post(index, username):
  posts = load_posts()
  if 0 <= index < len(posts):
    comment_content = input("Enter your comment: ").strip()
    new_comment = {"username": username, "content": comment_content}
    posts[index]["comments"].append(new_comment)
    save_posts(posts)
    print("Commment added!")
  else:
    print("Invalid post index.")

def get_topics(content):
  topics = re.findall(r'#\w+', content)
  # print(f"Extracted topics from post: {topics}")
  return topics

def count_topics(posts):
  topic_counter = Counter()
  for post in posts:
    topics = get_topics(post['content'])
    topic_counter.update(topics)
  # print(f"Topic counts: {topic_counter}")
  return topic_counter

def display_trending_topics(posts):
  topic_counter = count_topics(posts)
  trending_topics = [topic for topic, count in topic_counter.items() if count >= 5]
  if trending_topics:
    for topic in trending_topics:
      print(f"{topic}: {topic_counter[topic]} times")
  else: 
    print("No trending topics.")
