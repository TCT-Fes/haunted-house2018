#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 20:13:48 2018

@author: R-second
"""

#coding:utf-8
from requests_oauthlib import OAuth1Session
import json, config, os

# 環境変数をセット
# os.environ["HOGE"] = "FUGA"
# HOGEという環境変数にFUGAという文字列を入れる
username=config.username
passwd=config.passwd
proxyhost = "ccfw2.tu.tokuyama.ac.jp"
port = "8080"
os.environ["HTTP_PROXY"] = "http://{username}:{passwd}@{proxyhost}:{port}".format(
    username=username,
    passwd=passwd,
    proxyhost=proxyhost,
    port=port
)
os.environ["HTTPS_PROXY"] = "https://{username}:{passwd}@{proxyhost}:{port}".format(
    username=username,
    passwd=passwd,
    proxyhost=proxyhost,
    port=port
)

#４つのキーをセット
CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
# ツイート投稿用のURL（※）
url = "https://api.twitter.com/1.1/statuses/update.json"


# ツイート本文をstatusのバリューに設定


# OAuth認証で POST method で投稿
twitter = OAuth1Session(CK, CS, AT, ATS)
req = twitter.post(url, params = params)

# レスポンスを確認
if req.status_code == 200:
    print ("OK")
else:
    print ("Error: %d" % req.status_code)
