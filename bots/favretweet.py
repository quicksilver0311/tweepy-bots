#!/usr/bin/env python
# tweepy-bots/bots/favretweet.py
# This bot basically extracts all tweets from Tesla, SpaceX, Neuralink, The Boring Compnay and Elon Musk!

import tweepy
import logging
from config import create_api
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        keywords = ["TSLA", "$TSLA", "Tesla", "SpaceX", "Neuralink", "Boring"]
        logger.info(f"Processing tweet id {tweet.id}")
        
        if  hasattr(tweet, 'retweeted_status') or \
                tweet.in_reply_to_status_id is not None or \
                tweet.in_reply_to_screen_name is not None or\
                tweet.in_reply_to_user_id is not None or \
                tweet.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, ignore it
            return
        for keyword in keywords:
            if keyword in tweet.text:
                if not tweet.favorited:
                    # Mark it as Liked, since we have not done it yet
                    try:
                        tweet.favorite()
                    except Exception as e:
                        logger.error("Error on fav", exc_info=True)
                if not tweet.retweeted:
                    # Retweet, since we have not retweeted it yet
                    try:
                        tweet.retweet()
                        return
                    except Exception as e:
                        logger.error("Error on retweet", exc_info=True)
    def on_error(self, status):
        logger.error(status)

def main(users):
    api = create_api()
    tweets_listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(follow=users, languages=["en"])

if __name__ == "__main__":
    main(["44196397", "34743251", "13298072", "895332160130891776", "859816394556284929", "312562568"])
