import praw
import random
from time import sleep
from getSS import getSSfunc
from saveMp3func import saveMp3
from saveVideofunc import saveVideo


def createVideo(reddit, driver, name, bgcount):
    subreddit = reddit.subreddit(name)

    top_post = subreddit.top(time_filter="day", limit=1)

    for submission in top_post:
        if not submission.stickied and submission.is_self:
            print(submission.is_self)
            print(submission.ups)
            f = open('./textfiles/{}.txt'.format(submission.title[0:20]),"x")
            f.write("{}\n{}".format(submission.title, submission.selftext))
            print(submission.permalink)

            getSSfunc(driver, submission)

            saveMp3(submission)

            saveVideo(submission, bgcount , name)
