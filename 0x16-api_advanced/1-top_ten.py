#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=2".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    response = requests.get(url, headers=headers, allow_redirects=False).json()
    if response.get("error") == 404:
        print("None")
        return
    else:
        for obj in response.get("data").get("children"):
            print(obj.get("data").get("title"))
