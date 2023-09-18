import praw
import time
import os
import sys

reddit = praw.Reddit(
    client_id="B0eio-7aDAvaiw",
    client_secret="iSQezMpsgHspCQ7_C5Cx2bYNZZ8",
    user_agent="ehhebebehewwsdfxhjdgfs",
    username="NederlandseMemesbot",
    password="Pincode15",
)

subreddit = reddit.subreddit("nederlandsememes")


new = subreddit.new(limit=10)


for submission in new:
    if submission.distinguished == None:
        if submission.approved == True:
            submission.mod.flair(text="Toegestaan!", css_class="")
            print("Flair toegevoegd")
            
        else:
            print("nog niet toegestaan")

        
    else:
        print("skip omdat moderator")

print("------------------")
time.sleep(180)
os.execl(sys.executable, sys.executable, * sys.argv)
time.sleep(1)
