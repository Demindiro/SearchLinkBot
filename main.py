#!venv/bin/python3

from config import *
from praw import Reddit
from urllib.parse import quote_plus



"""
Globals
"""

reddit = Reddit(
    client_id     = CLIENT_ID,
    client_secret = CLIENT_SECRET,
    user_agent    = USER_AGENT,
    username      = USERNAME,
    password      = PASSWORD
)


"""
Search thing stuff
"""

def gen_link_google(string):
    return f'[Google](https://www.google.com/search?q={quote_plus(string)})'


def gen_link_ducks(string):
    return f'[DuckDuckGo](https://www.duckduckgo.com/{string})'


gen_link_functions = (
        gen_link_google,
        gen_link_ducks,
    )


"""
Main
"""

for submission in reddit.subreddit(SUBREDDIT).stream.submissions(skip_existing=True):
    if __debug__:
        print(submission.title)
    comment = '\n\n'.join((f(submission.title) for f in gen_link_functions))
    if __debug__:
        print(comment)
        print()
    submission.reply(comment)
