#!/usr/bin/env python
# tweepy-bots/bots/followfollowers.py
# This code basically gathers a list of followers every 60 secs and follows them back

import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def follow_followers(api):
    logger.info("Retrieving and following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logger.info(f"Following {follower.name}")
            try:
                follower.follow()
            except:
                logger.info("User " + follower.screen_name + " may have a private profile")  

def main():
    api = create_api()
    while True:
        follow_followers(api)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()
