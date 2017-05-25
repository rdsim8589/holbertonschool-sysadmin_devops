#!/usr/bin/python3
"""
module contains top_ten
"""
import requests
import random


def top_ten(subreddit):
    """
    find the top ten post of a subreddit
    input: subreddit
    return: titles of top 10 post of a subreddit or None
    """
    url = "https://www.reddit.com/r/{}/.json".format(subreddit)
    user_agent = "User Agent{:d}".format(random.randrange(1000, 9999))
    header = {'User-Agent': user_agent}
    r = requests.get(url, headers=header, allow_redirects=False)

    if r.status_code == 200:
        r_dict = r.json()
        try:
            for i in range(1, 11):
                print(r_dict["data"]['children'][i]['data']['title'])
        except Exception as e:
            print(e)
    else:
        print("None")
