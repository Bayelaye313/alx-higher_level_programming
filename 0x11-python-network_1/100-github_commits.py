#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository.

Usage: ./100-github_commits.py <repository name> <repository owner>
"""
import sys
import requests


if __name__ == "__main__":
    repname = sys.argv[1]
    repowner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(
        repowner, repname)

    req = requests.get(url)
    commits = req.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
