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
import pandas as pd

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
    foroba(auth)


def foroba(auth):
    # キーワードからツイートを取得
    follow_list = []
    api = tweepy.API(auth)
    follower_list = api.get_follower_ids(count=50)
    friend_list = api.get_friend_ids()
    print("現在フォローされてるid")
    print(follower_list)
    print("現在フォローしてるid")
    print(friend_list)
    for i in follower_list:
        if i not in friend_list:
            follow_list.append(i)
    print("今回フォローするid")
    print(follow_list)
    for followid in follow_list:
        if api.get_user(user_id=followid).protected:
            print("鍵垢検知")
        else:
            api.create_friendship(user_id=followid)
        time.sleep(1)


def csvcheck(passcsv):
    csvdata = []
    df = pd.read_table(passcsv)
    csvdata = df["name"]
    return csvdata

if __name__ == "__main__":
        main()