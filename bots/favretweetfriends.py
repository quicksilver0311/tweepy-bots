#!/usr/bin/env python
# tweepy-bots/bots/favretweet.py
# This bot retweets and likes all tweets from developer's friends

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
        logger.info(f"Processing tweet id {tweet.id}")
        
        if  tweet.in_reply_to_status_id is not None or \
                tweet.in_reply_to_screen_name is not None or\
                tweet.in_reply_to_user_id is not None or \
                tweet.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, ignore it
            return
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
    while 1:
        try:
            stream.filter(follow=users, languages=["en"], stall_warnings=True)
        except (ProtocolError, AttributeError):
            logger.error("Error on stream.filter", exc_info=True)

if __name__ == "__main__":
    main(["716563758634536960", "142721857", "239303217", "551104426", "1445615490", "312562568", "829308408", "71749635", "461147700", "1012185423248908289", "36420075","809522972805328896"])
