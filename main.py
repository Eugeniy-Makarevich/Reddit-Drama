#import modules
import praw, csv, os

# function appends row to file
def append_record(record):
    with open('reddit_drama.csv', 'a',encoding = 'utf-8',newline = '') as f:
        writer = csv.writer(f,delimiter = ';')
        writer.writerow(record)

# get file last-modified date or create new file 
try:
    last_modified = os.path.getmtime('reddit_drama.csv')
except:
    last_modified = 0
    # write header   
    header = ['title','upvotes','author','comments','upvote_ratio','created'] 
    append_record(header)

# new last_modified time to set after script execution    
set_modified = last_modified

#initialize PRAW and get subreddit
reddit = praw.Reddit("BOT")
subreddit = reddit.subreddit("subredditdrama")

# function returns generator with info about submissions in subreddit-new. 
def scrape_hot(n_last_submissions):
    for submission in subreddit.new(limit = n_last_submissions):
        if submission.created > last_modified:
            yield [ submission.title,
                   submission.score,
                   submission.author.name if submission.author 
                                        else 'deleted',
                   submission.num_comments,
                   submission.upvote_ratio,
                   submission.created ]
        else : break
                                    
# write file             
for row in scrape_hot(1000):
    append_record(row)
    if row[5] > set_modified:
        set_modified = row[5]

# set modification time equal last submission created             
os.utime('reddit_drama.csv',(set_modified,set_modified))              
         

