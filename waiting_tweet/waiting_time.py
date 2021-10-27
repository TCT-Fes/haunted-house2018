111#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 10:27:36 2018

@author: R-second
"""

import csv, config, os, json

time=8
now=0
cnt=0
waiting=0
"data=[5]"
fuga=[]

with open("C:\\Users\\Mirai\\Desktop\\tweet\\data.csv","r") as f:
    csv_data = csv.reader(f)
    for data in csv_data:
            fuga=data
            break

print(fuga)
now = int(fuga[0])
cnt = int(fuga[1])
waiting = int(fuga[2])
print(now,cnt,waiting)

f.close()

data_list=[]
with open("C:\\Users\\Mirai\\Desktop\\tweet\\password.csv", encoding="utf_8") as csvfile:
    csv_data = csv.reader(csvfile)
    for row in csv_data:
        #appendで格納。print(row)を入れてみると分かり易いかも。
        data_list.append(row)

#coding:utf-8
from requests_oauthlib import OAuth1Session
#４つのキーをセット
CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

username=config.username
passwd=config.passwd
proxyhost = "ccfw2.tu.tokuyama.ac.jp"
port = "8080"
# ツイート投稿用のURL（※）
url = "https://api.twitter.com/1.1/statuses/update.json"

os.environ["HTTPS_PROXY"] = "https://{username}:{passwd}@{proxyhost}:{port}".format(
    username=username,
    passwd=passwd,
    proxyhost=proxyhost,
    port=port
)

while(True):
    try:
        suuti=int(input("人が入ったら1, 整理券を発行したい場合は2,パスワードを確認する場合は3を入力してください。\n\n終了したい場合はCtrlとCを同時に押してください。\n\n"))

        if(suuti==1):
            now=now+1
            print("今、中に%s番目の人が入っています\n\n\n" % now)


        if(cnt<now):
            cnt=cnt+1

        if(suuti==2):
            cnt=cnt+1
            print("今、%s番目の人が待っています。" % cnt)
            waiting=time*(cnt-now-1)
            print("待ち時間は%s分です" % waiting)
            print("パスコードは%sです\n\n\n" % data_list[cnt-1])

        with open("C:\\Users\\Mirai\\Desktop\\tweet\\data.csv","w") as f:
           writer = csv.writer(f)
           writer.writerow([now,cnt,waiting])
           f.close()

# ツイート本文をstatusのバリューに設定
        if(suuti==9):
            params = {"status": "あと５分後くらいに整理券の発行を行います。７枚発行予定で状況によって変動します。"}

# OAuth認証で POST method で投稿
            twitter = OAuth1Session(CK, CS, AT, ATS)
            req = twitter.post(url, params = params)

# レスポンスを確認
            if req.status_code == 200:
                print ("OK")
                
            else:
                print ("Error: %d" % req.status_code)

        if(suuti==3):
            print("あなたのパスワードは%sです。" % data_list[now])

    except ValueError:
        print("入力にミスがあります。")
        pass
