#!/usr/bin/env python
# tweepy-bots/bots/updatestatus.py
# This code is a one time setup code for description and first tweet.

import tweepy
from config import create_api

def main():
    api = create_api()
    #api.update_status("I belong to @quicksilver0311. I follow followers!")
    api.update_profile(description="I was born on July 11, 2020. I belong to @quicksilver0311. All tweets are retweets! I evolve. I change. I grow!")

if __name__ == "__main__":
    main()
