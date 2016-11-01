import praw
import time
import re

# Insert your username and password here 
username = ""
password = ""
r = praw.Reddit(user_agent = "Counts people who say alot")
word_to_match = [r'\balot\b']
# While bot is running insert them here to count
storage = []
r.login(username, password)

def run_bot():
	subreddit = r.get_subreddit("all")
	print("Grabbing subreddit")
	comments = subreddit.get_comments(limit=200)
	print("Grabbing comments")
	for comment in comments:
		comment_text = comment.body.lower()
		isMatch = any(re.search(string, comment_text) for string in word_to_match)
		if comment.id not in storage and isMatch and comment.author not in storage:
			print("Match found! Storing username: " + str(comment.author) + " into storage.")
            print(comment_text)
			storage.append(comment.author)

	print("There are currently: " + str(len(storage)) + " people who use 'alot' instead of ' a lot'.")

while True:
	run_bot()
	time.sleep(2)