import praw
import os

reddit = praw.Reddit("BOT")
print(reddit.read_only)
for submission in reddit.subreddit("test").hot(limit=10):
    print(submission.title)