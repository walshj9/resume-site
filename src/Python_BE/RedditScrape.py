#!/bin/python3
import os
import praw
import csv
import datetime
from configparser import ConfigParser

config = ConfigParser()

try: #stops a weird behavior where program runs in vscode but not terminal
    directory = os.getcwd()
    config.read(f'{directory}/src/Python_BE/login_info.ini')

    reddit = praw.Reddit(
    client_id=config['Login_Data']['id'],
    client_secret=config['Login_Data']['secret'],
    user_agent=config['Login_Data']['user_agent'],
    username=config['Login_Data']['username'],
    password=config['Login_Data']['password']
    )
except:#runs in terminal
    config.read('login_info.ini')

    reddit = praw.Reddit(
    client_id=config['Login_Data']['id'],
    client_secret=config['Login_Data']['secret'],
    user_agent=config['Login_Data']['user_agent'],
    username=config['Login_Data']['username'],
    password=config['Login_Data']['password']
)



#sets script to read only
reddit.read_only = True

timestamp = str(datetime.datetime.now()) #string timestamp for subscript
timestamp = timestamp[:-10] #shaves off seconds
chars_to_replace = {
    ' ' : '',
    '-' : '',
    ':' : ''
}
timestamp = timestamp.translate(str.maketrans(chars_to_replace)) #timestamp format YYYYMMDDhhmm

#id, author, title, score, num_comments, subreddit, permalink, over_18
fields = ['id', 'author', 'title', 'score','num_comments', 'subreddit', 'permalink', 'over_18']
with open(f'{timestamp}.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(fields)
    for submission in reddit.subreddit("all").hot(limit=100): 
        data = [submission.id, submission.author, submission.title, submission.score,
        submission.num_comments, submission.subreddit, submission.permalink, submission.over_18]
        writer.writerow(data)
    