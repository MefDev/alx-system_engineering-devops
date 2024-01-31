#!/usr/bin/python3

import requests


def top_ten(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False).json()
    if response.get("error") == 404:
        print("None")
        return
    for obj in response.get("data").get("children"):
        print(obj.get("data").get("title"))
