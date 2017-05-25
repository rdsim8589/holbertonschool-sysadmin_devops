#!/usr/bin/python3
"""
contains number_of_subscribers method
"""
import requests


def number_of_subscribers(subreddit):
    """
    check subreddit subscriber number count
    input: subreddit
    return: number of subreddit subscribers or 0
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        'User-Agent': 'My User Agent 1.0'
        }
    r = requests.get(url, headers=headers)
    if r.status_code == 404:
        return 0
    subs = r.json()['data'].get('subscribers', 0)
    return subs
