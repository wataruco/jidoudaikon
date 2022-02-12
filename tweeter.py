# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 06:07:39 2021

@author: watar
"""

# This Python file uses the following encoding: utf-8
# pip install android-auto-play-opencv

 
#csvに収めたキーを利用して特定の言葉を含むツイートを取得する

from ast import keyword
import tweepy
import twitter
import os
import csv
import logging

# 認証に必要なキーとトークン


API_KEY = ""
API_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""
keypasscsv = 'C:\\Users\watar\OneDrive\Documents\\twipass.csv'
def main():
    logging.basicConfig()
    logger = logging.getLogger(__name__)
    keypass = csvcheck(keypasscsv)

    API_KEY = keypass[0]
    API_SECRET = keypass[1]
    ACCESS_TOKEN = keypass[2]
    ACCESS_TOKEN_SECRET = keypass[3]
    # APIの認証
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    tweet_ward = "私は大根様のしもべです"      #ツイートする言葉
    cli = tweepy.Client(consumer_key=API_KEY, consumer_secret=API_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)
    tweeter(cli,tweet_ward)


def tweeter(cli,tweet_ward):
    print(tweet_ward)
    # ツイートを投稿
    cli.create_tweet(text=tweet_ward)


def csvcheck(passcsv):      #csvを呼んでリストにして返す
    csvdata = []
    with open(passcsv) as f:
        reader = csv.reader(f)
        for row in reader:
            csvdata.append(row[0])
    return csvdata

if __name__ == "__main__":
        main()