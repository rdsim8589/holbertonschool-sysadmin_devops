#!/usr/bin/python3
"""
Contains the recurse method
"""
import requests
import random


def recurse(subreddit, hot_list=[]):
    """
    Creates a list of all the titles of the hot list
    input:
        subreddit: the name of a reddit subreddit
        hot_list: list to be filled with the sub reddit name
    return: host_list or None otherwise
    """
    user_agent = "User Agent{:d}".format(random.randrange(1000, 9999))
    header = {'User-Agent': user_agent}
    after = ""
    while True:
        url = "https://www.reddit.com/r/{}/.json{}".format(subreddit, after)
        r = requests.get(url, headers=header, allow_redirects=False)
        if r.status_code == 200:
            r_dict = r.json()
            for reddit_post in r_dict["data"]["children"]:
                hot_list.append(reddit_post['data']['title'])
            after = r_dict['data']['after']
            if after is None:
                break
            after = "?after={}".format(after)
        else:
            return None
    return hot_list
