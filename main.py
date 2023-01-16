#import modules
import praw
import pprint

#initialize PRAW and get subreddit
reddit = praw.Reddit("BOT")
subreddit = reddit.subreddit("subredditdrama")

def scrape_hot(n_last_submissions):
    for submission in subreddit.hot(limit = n_last_submissions):
        yield {
              'title' : submission.title,
               'upvote' : submission.score,
               'author' : submission.author,
               'num_comments' : submission.num_comments,
               'upvote_ratio' : submission.upvote_ratio,
               'created'      : submission.created_utc
               }
               
               
               
               
               
         

