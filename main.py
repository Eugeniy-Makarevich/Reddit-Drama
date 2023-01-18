#import modules
import praw, csv

#initialize PRAW and get subreddit
reddit = praw.Reddit("BOT")
subreddit = reddit.subreddit("subredditdrama")

# function returns generator with info about submissions in subreddit - new. 
def scrape_hot(n_last_submissions):
    for submission in subreddit.new(limit = n_last_submissions):
        yield [ submission.title,
                submission.score,
                submission.author.name if submission.author 
                                        else 'deleted',
                submission.num_comments,
                submission.upvote_ratio,
                submission.created_utc ]
                         
# function appends row to file
def append_record(record):
    with open('reddit_drama.csv', 'a',encoding = 'utf-8',newline = '') as f:
        writer = csv.writer(f,delimiter = ';')
        writer.writerow(record)
        
# write header   
header = ['title','upvotes','author','comments','upvote_ratio','created'] 
append_record(header)
           
# write file             
for row in scrape_hot(1000):
       append_record(row)           
               
               
         

