#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    url = "https://www.reddit.com/r/{subreddit}/about.json". format(subreddit)
    headers = {'User-Agent': 'my-subreddit-subscriber-count/0.1'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 404:
            return 0
        results = response.json().get("data", {})
        return results.get("subscribers", 0)
    except requests.RequestException:
        return 0
