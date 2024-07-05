#!/usr/bin/python3
"""Uses the GitHub API to display a GitHub ID based on given credentials.

Usage: ./10-my_github.py <GitHub username> <GitHub password>
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    gituser = sys.argv[1]
    gitpass = sys.argv[2]
    auth = HTTPBasicAuth(gituser, gitpass)
    req = requests.get("https://api.github.com/user", auth=auth)
    print(req.json().get("id"))
