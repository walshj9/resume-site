from sqlite3 import Timestamp
from time import time
import praw
import configparser
import csv
import datetime

config = configparser.ConfigParser()

config.read('reddit_login.ini')

#login info for OAuth
id = config['Information']['id']
secret = config['Information']['secret']
agent = config['Information']['user_agent']
uname = config['Information']['username']
passphrase = config['Information']['password']

reddit = praw.Reddit(
    client_id=id,
    client_secret=secret,
    user_agent=agent,
    username=uname,
    password=passphrase
)

#sets script to read only
reddit.read_only = True

for submission in reddit.subreddit("all").hot(limit=10):
    print(submission.score)

timestamp = str(datetime.datetime.now()) #string timestamp for subscript
timestamp = timestamp[:-10] #shaves off seconds

chars_to_replace = {
    ' ' : '',
    '-' : '',
    ':' : ''
}

timestamp = timestamp.translate(str.maketrans(chars_to_replace)) #timestamp format YYYYMMDDhhmm

