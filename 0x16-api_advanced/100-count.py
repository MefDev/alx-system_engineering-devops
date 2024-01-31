#!/usr/bin/python3
"""Module 4"""
import requests


def count_words(subreddit, word_list):
    """parses the title of all hot articles, and prints a sorted count of given keywords ("""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False).json()
    if response.get("error") == 404:
        return None
    for obj in response.get("data").get("children"):
        word_list.append(obj.get("data").get("title"))
        after = response.get("data").get("after")
        if after:
            url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
                subreddit, after)
            headers = {"User-Agent": "My-User-Agent"}
            response = requests.get(url, headers=headers,
                                    allow_redirects=False).json()
            for obj in response.get("data").get("children"):
                word_list.append(obj.get("data").get("title"))
            after = response.get("data").get("after")
            if after:
                count_words(subreddit, word_list)
