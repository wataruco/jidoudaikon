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
from datetime import datetime,timezone
import pytz
import pandas as pd

# 認証に必要なキーとトークン


API_KEY = ""
API_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""
keypasscsv = '..\..\\twipass.csv'
def main():
    logging.basicConfig()
    logger = logging.getLogger(__name__)
    keypass = csvcheck(keypasscsv)
    searcharray = csvcheck("search.csv")
    trendharray = csvcheck("..\..\datastrage\\trend\\trend.csv")

    API_KEY = keypass[0]
    API_SECRET = keypass[1]
    ACCESS_TOKEN = keypass[2]
    ACCESS_TOKEN_SECRET = keypass[3]
    # APIの認証
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    math = 45                   #検索する数
    twisearch(auth,searcharray,math)
    twisearch(auth,trendharray,math)


def twisearch(auth,searcharray,math):
    # キーワードからツイートを取得
    api = tweepy.API(auth)
    for search_ward in searcharray:
        tweets = api.search_tweets(q=search_ward, count=math)
        now = datetime.now()
        filename = 'C:\\Users\watar\OneDrive\Documents\datastrage\RawData\\' + search_ward + " " + now.strftime('%Y%m%d_%H') + '.csv'
        print(filename + "記述")
        f = open(filename, 'a', encoding="utf_8_sig")
        for tweet in tweets:
            writeline = str(tweet.user.id) + "," + tweet.user.screen_name + "," + change_time_JST(tweet.created_at) + ",\"" + tweet.text + "\"" + "\n"
            f.writelines(writeline)
        time.sleep(3)
        


def csvcheck(passcsv):      #csvを呼んでリストにして返す
    csvdata = []
    with open(passcsv) as f:
        reader = csv.reader(f)
        for row in reader:
            csvdata.append(row[0])
    return csvdata

def change_time_JST(u_time):
    #イギリスのtimezoneを設定するために再定義する
    utc_time = datetime(u_time.year, u_time.month,u_time.day, \
    u_time.hour,u_time.minute,u_time.second, tzinfo=timezone.utc)
    #タイムゾーンを日本時刻に変換
    jst_time = utc_time.astimezone(pytz.timezone("Asia/Tokyo"))
    # 文字列で返す
    str_time = jst_time.strftime("%Y-%m-%d_%H:%M:%S")
    return str_time

if __name__ == "__main__":
        main()