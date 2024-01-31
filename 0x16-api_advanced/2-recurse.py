#!/usr/bin/python3

import requests


def recurse(subreddit, hot_list=[]):
    """Returns the number of subscribers for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False).json()
    if response.get("error") == 404:
        return None
    for obj in response.get("data").get("children"):
        hot_list.append(obj.get("data").get("title"))
    after = response.get("data").get("after")
    if after:
        url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
            subreddit, after)
        headers = {"User-Agent": "My-User-Agent"}
        response = requests.get(url, headers=headers,
                                allow_redirects=False).json()
        for obj in response.get("data").get("children"):
            hot_list.append(obj.get("data").get("title"))
        after = response.get("data").get("after")
        if after:
            recurse(subreddit, hot_list)
    return hot_list
