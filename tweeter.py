# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 06:07:39 2021

@author: watar
"""

# This Python file uses the following encoding: utf-8
# pip install android-auto-play-opencv

 
#csvに収めた言葉の中からランダムに選択してツイートを行う

from ast import keyword
from fileinput import filename
import tweepy
import twitter
import os
import csv
import logging
import random
import pandas as pd

# 認証に必要なキーとトークン


API_KEY = ""
API_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""
keypasscsv = 'C:\\Users\watar\OneDrive\Documents\\twipass.csv'
twitextpass =  'agatha.csv'
def main(picfilename):
    tweet_ward = []
    logging.basicConfig()
    logger = logging.getLogger(__name__)
    keypass = csvcheck(keypasscsv)
    # twiarray = csvcheck(twitextpass)
    # tweet_ward = "データ収集中・・・ pythonより投稿テスト\n" + twiarray[random.randint(0,len(twiarray)-1)]
    trend = picfilename.replace("..\..\datastrage\wordcroud\\","")
    trend = trend[:-16]
    tweet_ward.append("トレンドの情報を画像に集めます")
    tweet_ward.append("対象のトレンドワードは「" + trend + "」です")
    twittertext='\n'.join(tweet_ward)

    API_KEY = keypass[0]
    API_SECRET = keypass[1]
    ACCESS_TOKEN = keypass[2]
    ACCESS_TOKEN_SECRET = keypass[3]
    
    
    # APIの認証
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    cli = tweepy.Client(consumer_key=API_KEY, consumer_secret=API_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)
    tweeter(cli,twittertext)
    # cli.create_tweet(status=tweet_ward, filename='testgazou.png')
    api.update_status_with_media(status = twittertext, filename = picfilename)


def tweeter(cli,tweet_ward):
    print(tweet_ward)
    # ツイートを投稿
    # cli.create_tweet({"text": "pythonより画像付きツイートテスト","media": "testgazou.png"})


def csvcheck(passcsv):
    csvdata = []
    df = pd.read_table(passcsv)
    csvdata = df["name"]
    return csvdata

if __name__ == "__main__":
        main()