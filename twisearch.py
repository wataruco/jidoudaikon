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
import os
import csv
import logging
import time
import datetime

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
    search_ward = "VTuber"      #検索する言葉
    math = 30                   #検索する数
    twisearch(auth,search_ward,math)


def twisearch(auth,search_ward,math):
    # キーワードからツイートを取得
    api = tweepy.API(auth)
    tweets = api.search_tweets(q=search_ward, count=math)
    now = datetime.datetime.now()
    filename = 'C:\\Users\watar\OneDrive\Documents\datastrage\\' + search_ward + " " + now.strftime('%Y%m%d_%H%M%S') + '.txt'
    f = open(filename, 'w', encoding='UTF-8')

    for tweet in tweets:
        print('-----------------')
        print(tweet.text)
        f.writelines(tweet.text)
        f.writelines('\n-----------------\n')
        


def csvcheck(passcsv):      #csvを呼んでリストにして返す
    csvdata = []
    with open(passcsv) as f:
        reader = csv.reader(f)
        for row in reader:
            csvdata.append(row[0])
    return csvdata

if __name__ == "__main__":
        main()