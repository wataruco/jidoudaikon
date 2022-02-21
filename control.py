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
import twitrend
import followback

# 認証に必要なキーとトークン


API_KEY = ""
API_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""
keypasscsv = 'C:\\Users\watar\OneDrive\Documents\\twipass.csv'
twitextpass =  'agatha.csv'
def main():
    schedule.every(30).minutes.do(dojob)
    dojob()
    while True:
        schedule.run_pending()
        time.sleep(1)

def dojob():
    filename = twitrend.main()
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