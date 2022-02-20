#ライブラリのインポート
import tweepy
from datetime import datetime,timezone
import pytz
import pandas as pd
import os
import schedule
from time import sleep #t
import csv

def main():
    #ターミナルに現在時刻を出力
    print(datetime.now())
    #Twitterの認証
    API_KEY = ""
    API_SECRET = ""
    ACCESS_TOKEN = ""
    ACCESS_TOKEN_SECRET = ""
    keypasscsv = 'C:\\Users\watar\OneDrive\Documents\\twipass.csv'

    keypass = csvcheck(keypasscsv)
    searcharray = csvcheck("search.csv")
    trenharray = csvcheck("..\..\datastrage\\trend\\trend.csv")
    trend15 = trenharray[0:20]
    item_num = 30    #ツイッターのサーチ数
    API_KEY = keypass[0]
    API_SECRET = keypass[1]
    ACCESS_TOKEN = keypass[2]
    ACCESS_TOKEN_SECRET = keypass[3]
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    for searchword in searcharray:
        twicsv(searchword,item_num,api)
        sleep(1)    
    for searchword in trend15:
        twicsv(searchword,item_num,api)
        sleep(1)

def twicsv(searchkey,item_num,api):
    tweets = tweepy.Cursor(api.search_tweets,q=searchkey,lang='ja').items(item_num)
    #抽出したデータから必要な情報を取り出す
    #取得したツイートを一つずつ取り出して必要な情報をtweet_dataに格納する
    tweet_data = []
    for tweet in tweets:
        #ツイート時刻とユーザのアカウント作成時刻を日本時刻にする
        tweet_time = change_time_JST(tweet.created_at)
        create_account_time = change_time_JST(tweet.user.created_at)
        #tweet_dataの配列に取得したい情報を入れていく
        tweet_data.append([
            tweet.id,
            tweet_time,
            tweet.text,
            tweet.favorite_count, 
            tweet.retweet_count, 
            tweet.user.id, 
            tweet.user.screen_name,
            tweet.user.name,
            tweet.user.description,
            tweet.user.friends_count,
            tweet.user.followers_count,
            create_account_time,
            tweet.user.following,
            tweet.user.profile_image_url,
            tweet.user.profile_background_image_url,
            tweet.user.url
                           ])
    #CSVファイルに出力するときの列の名前を定義
    labels=[
        'ツイートID',
        'ツイート時刻',
        'ツイート内容',
        'いいね数',
        'リツイート数',
        'ID',
        'ユーザID',
        'アカウント名',
        '自己紹介文',
        'フォロー数',
        'フォロワー数',
        'アカウント作成日時',
        '自分がフォローしているか？',
        'アイコン画像URL',
        'ヘッダー画像URL',
        'WEBサイト'
        ]
    #tweet_dataのリストをpandasのDataFrameに変換
    df = pd.DataFrame(tweet_data,columns=labels)
    #--- ここから新しい内容 ---
    #csvのファイル名
    file_name="..\..\datastrage\RawData\\" + searchkey + ".csv"
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
        #csvファイルの読み込み
        df_csv = pd.read_csv(file_name)
        #縦方向に-データフレームを結合
        df_merge = pd.concat([df_csv,df])
        #ツイートIDが重複しているものを削除
        df_merge = df_merge.drop_duplicates(keep='last',subset='ツイートID')
        #csvファイル出力
        df_merge.to_csv(file_name,encoding='utf-8-sig',index=False)

#関数:UTCをJSTに変換する
def change_time_JST(u_time):  
    #イギリスのtimezoneを設定するために再定義する
    utc_time = datetime(u_time.year, u_time.month,u_time.day, \
    u_time.hour,u_time.minute,u_time.second, tzinfo=timezone.utc)   # datetimeに変換(timezoneを付与)
    #タイムゾーンを日本時刻に変換
    jst_time = utc_time.astimezone(pytz.timezone("Asia/Tokyo"))
    #2021-09-26_17:19:20  という形式の文字列を返す
    str_time = jst_time.strftime("%Y-%m-%d_%H:%M:%S")
    return str_time

#csvを呼んでリストにして返す
def csvcheck(passcsv):
    csvdata = []
    df = pd.read_table(passcsv)
    csvdata = df["name"]
    return csvdata

if __name__ == "__main__":
        main()