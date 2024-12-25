import praw
from selenium import webdriver
from loginfunc import openLogin
from mainvideofunc import createVideo

username = "reddit_username"
password = "reddit_password"

driver = webdriver.Chrome()

openLogin(driver, password, username)

reddit = praw.Reddit(
    client_id="bot_clientid",
    client_secret="bot_clientSecret",
    password="reddit_pass",
    user_agent="bot_name",
    username="reddit_usename",
)

print("Login successful")



#########################################################################################################################
"""
    important commands : 
    https://praw.readthedocs.io/en/latest/code_overview/models/submission.html#praw.models.Submission    
"""
########################################################################################################################


bgcount = 1

listsub = []
n = int(input("Number of Subreddits : "))
for i in range(n):
    a = input("name of subreddit : ")
    listsub.append(a)

for sub in listsub:

    createVideo(reddit, driver, sub, bgcount)
