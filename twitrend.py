# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 06:07:39 2021

@author: watar
"""

# This Python file uses the following encoding: utf-8
# pip install android-auto-play-opencv

 
#csvに収めたキーを利用して特定の言葉を含むツイートを取得する

from ast import While, keyword
from lib2to3.pytree import WildcardPattern
from numpy import true_divide
import numpy as np
import tweepy
import os
import csv
import logging
import time
import datetime
from datetime import datetime,timezone
import pytz
import pandas as pd
import random
import wordcroudmake
import twicsv
import trendanalize

# 認証に必要なキーとトークン


API_KEY = ""
API_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""
keypasscsv = 'C:\\Users\watar\OneDrive\Documents\\twipass.csv'
file_name2="..\..\datastrage\\trend\\trendrireki.csv"
def main():
    logging.basicConfig()
    logger = logging.getLogger(__name__)
    keypass = csvcheck(keypasscsv)
    rirekiarray = csvcheck(file_name2)

    API_KEY = keypass[0]
    API_SECRET = keypass[1]
    ACCESS_TOKEN = keypass[2]
    ACCESS_TOKEN_SECRET = keypass[3]
    # APIの認証
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    woeid = 23424856                   #日本のコード
    trend = twitrendget(auth,woeid)
    print("トレンド取得 1位は" + trend[0])
    #tweet_dataのリストをpandasのDataFrameに変換
    df = pd.DataFrame(trend)
    #--- ここから新しい内容 ---
    #csvのファイル名
    now = datetime.now()
    file_name="..\..\datastrage\\trend\old\\trend" + " " + now.strftime('%Y%m%d_%H%M') + '.csv'
    csvmake(file_name,df)
    csvmake("..\..\datastrage\\trend\\trend.csv",df)
    twicsv.main()
    datacsv = csvcheck("..\..\datastrage\\trend\\trend.csv")
    select_trend = datacsv[random.randint(0,14)]
    print("選択ワード:"+select_trend)
    while True:
        if trendanalize.analize(select_trend,rirekiarray[0])==False:
            print("データ被り:"+select_trend+"と"+datacsv[0])
            select_trend = datacsv[random.randint(0,29)]
            print("再選択ワード:"+select_trend)
            print(select_trend)
        elif trendanalize.analize(select_trend,rirekiarray[1])==False:
            print("データ被り:"+select_trend+"と"+datacsv[1])
            select_trend = datacsv[random.randint(0,29)]
            print("再選択ワード:"+select_trend)
            print(select_trend)
        elif trendanalize.analize(select_trend,rirekiarray[2])==False:
            print("データ被り:"+select_trend+"と"+datacsv[2])
            select_trend = datacsv[random.randint(0,29)]
            print("再選択ワード:"+select_trend)
            print(select_trend)
        elif select_trend in rirekiarray.tolist():
            select_trend = datacsv[random.randint(0,29)]
            print("データ被り")
            print(select_trend)
        else:
            rirekiarray = np.roll(rirekiarray,1)
            rirekiarray[0] = select_trend
            df = pd.DataFrame(data = {'name':rirekiarray})
            df.to_csv(file_name2,encoding='utf-8-sig',index=False)
            break

    # while True:
    #     if select_trend in rirekiarray.tolist():
    #         select_trend = datacsv[random.randint(0,19)]
    #         print("データ被り")
    #         print(select_trend)
    #     else:
    #         rirekiarray = np.roll(rirekiarray,1)
    #         rirekiarray[0] = select_trend
    #         df = pd.DataFrame(data = {'name':rirekiarray})
    #         df.to_csv(file_name2,encoding='utf-8-sig',index=False)
    #         break


    filename = wordcroudmake.wordcroudmaker(select_trend)
    return filename


def csvmake(file_name,df):
    #カレントディレクトリを取得
    current_path = os.getcwd()
    #csvファイルの絶対パス
    file_path = os.path.join(current_path,file_name)
    #カレントディレクトリにtweet.csvが存在するか？
    file_check = os.path.isfile(file_path)
    #同じ名前のファイルがないとき
    if not file_check:  
        df.to_csv(file_name,encoding='utf-8-sig',index=False)
    #すでに同じファイルが存在しているとき
    else:
        df.to_csv(file_name,encoding='utf-8-sig',index=False)

def twitrendget(auth,woeid):
    # キーワードからツイートを取得
    api = tweepy.API(auth)
    #トレンド一覧取得
    trends = api.get_place_trends(woeid)
    naradeha = api.available_trends()

    #データフレームに変換
    import pandas as pd
    df = pd.DataFrame(trends[0]["trends"])
    return df["name"]
            


def csvcheck(passcsv):
    csvdata = []
    df = pd.read_table(passcsv)
    csvdata = df["name"]
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