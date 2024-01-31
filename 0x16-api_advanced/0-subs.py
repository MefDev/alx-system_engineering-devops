#!/usr/bin/python3

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False).json()
    if response.get("error") == 404:
        return 0
    return response.get("data").get("subscribers")
