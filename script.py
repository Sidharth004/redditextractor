import praw
from datetime import datetime
from dotenv import load_dotenv
import time
import os

load_dotenv()


print('all libraries imported')
print('current time',datetime.now())

#get credientiols 
client_id=os.getenv('REDDIT_CLIENT_ID')
client_secret=os.getenv('REDDIT_CLIENT_SECRET')


#check if credentioals are loaded
if not client_id or not client_secret:
    print('ERROR - Credentioal snot found')
    exit()

print('credentials loaded form dot evnv files succesfully');

#connect to reddit

reddit = praw.Reddit(
    client_id = client_id,
    client_secret = client_secret,
    user_agent ='TestScript/1.0'
)

print('CONNECTED!')
print("Read only mode",reddit.read_only)


