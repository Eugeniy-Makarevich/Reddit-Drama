#import modules
import praw, json

#initialize PRAW and get subreddit
reddit = praw.Reddit("BOT")
subreddit = reddit.subreddit("subredditdrama")

# function returns generator with info about submissions in subreddit - new. 
def scrape_hot(n_last_submissions):
    for submission in subreddit.new(limit = n_last_submissions):
        yield {
              'title' : submission.title,
               'upvote' : submission.score,
               'author' : submission.author.name if submission.author 
                                                 else 'deleted',
               'num_comments' : submission.num_comments,
               'upvote_ratio' : submission.upvote_ratio,
               'created'      : submission.created_utc
               }
        
# function appends row to file
def append_record(record):
    with open('reddit_drama.txt', 'a') as f:
        json.dump(record, f)
        f.write('\n') 
              
# write file             
for row in scrape_hot(1000):
       append_record(row)           
               
               
         

