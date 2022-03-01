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
import random
import tweeter
import twisearch
import twicsv
import time
import schedule
import twitrend2
import followback

# 認証に必要なキーとトークン


API_KEY = ""
API_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""
keypasscsv = '..\..\\twipass.csv'
twitextpass =  'agatha.csv'
def main():
    try:
        filename = twitrend2.main()
    except Exception as e:
        print("エラーなので一回休みです")
        print(e)
    else:
        followback.main()
        tweeter.main(filename)



def csvcheck(passcsv):      #csvを呼んでリストにして返す
    csvdata = []
    with open(passcsv) as f:
        reader = csv.reader(f)
        for row in reader:
            csvdata.append(row[0])
    return csvdata

if __name__ == "__main__":
        main()