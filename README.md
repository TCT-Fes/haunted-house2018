# haunted-house2018
2018年のお化け屋敷のコード集です。

公式Webページは<a data-from-md title='https://tct-fes.github.io/haunted-house2018/'
            href='https://tct-fes.github.io/haunted-house2018/' target="_blank" rel="noopener noreferrer">ここ</a>

<br>

# ディレクトリ構成

```bash
haunted-house2018
├── LICENSE
├── README.md
├── __MACOSX
├── favicon.ico
├── index.css
├── index.html
├── map.png
├── sensor              # Arduinoのコード
│   ├── kansei.py       # Pythonでシリアル通信 + 音を鳴らす
│   └── sensor
│       └── sensor.ino
├── test.txt
└── waiting_tweet         # 広報用のTwitter Botのコード？
    ├── GetTimelines.py
    ├── PostTweet.py
    ├── config.py
    ├── data.csv
    ├── password.csv
    └── waiting_time.py
```



## sensor
- Arduinoで距離を計測
- 距離のデータによって、音を制御

<br>

## waiting_tweet

- 受付のPCで待ち人数と入った人数を管理
- 待ち時間を自動で計算し、定期的に自動ツイート
- アクセストークン部分は空にしてあります




