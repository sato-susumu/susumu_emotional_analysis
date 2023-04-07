## 概要
テキストを入力として受け取り、感情情報(喜び、悲しみ、期待、驚き、怒り、恐れ、嫌悪)を推定して返すサーバーです。
[WRIME: 主観と客観の感情分析データセット](https://github.com/ids-cv/wrime)でモデルを作り、 そのモデルをサーバーで利用しています。

## 動作確認環境
Windows 11  
Ubuntu 22.04 on WSL

## 動作方法
### Windows
#### 必要な準備
Docker Desktop, git

#### 準備
コマンドラインで次の内容を実行
```
git clone https://github.com/sato-susumu/susumu_emotional_analysis.git
cd susumu_emotional_analysis
```

#### 起動
コマンドラインで次の内容を実行。初回などイメージのビルドが行われる場合は時間がかかります。サーバーの起動にも少し時間がかかります。
```
start_server.bat
```

#### 呼び出し例
PowerShell上で次の内容を実行
```
Invoke-RestMethod -Uri http://127.0.0.1:56563/analyze_emotion -Method Post -ContentType 'application/json' -Body ('{"text":"いい天気だ"}')
```

呼び出し結果
```
emotions
--------
@{Joy=0.046955835074186325; Sadness=0.014234731905162334; Anticipation=0.10810994356870651; Surprise=0.7903380990028381; Anger=0.0037900868337601423; Fear=0.021550703793764114; Disgust=0.01135258749127388; Trust=0.003668030956760049}
```


#### 停止
コマンドラインで次の内容を実行
```
stop_server.bat
```


### Ubuntu
#### 準備
コマンドラインで次の内容を実行
```
git clone https://github.com/sato-susumu/susumu_emotional_analysis.git
cd susumu_emotional_analysis
```

#### 起動
コマンドプロンプトで次の内容を実行。初回などイメージのビルドが行われる場合は時間がかかります。サーバーの起動にも少し時間がかかります。
```
./start_server.sh
```

#### 呼び出し例
コマンドプロンプトで次の内容を実行
```
curl -X POST -H "Content-Type: application/json" -d '{"text":"いい天気だ"}' http://127.0.0.1:56563/analyze_emotion
```

呼び出し結果
```
{"emotions":[{"Joy":0.8913211822509766,"Sadness":0.0037260549142956734,"Anticipation":0.03549545258283615,"Surprise":0.03090864047408104,"Anger":0.000993472058326006,"Fear":0.002147842664271593,"Disgust":0.0024142847396433353,"Trust":0.03299309313297272}]}
```

#### 停止
コマンドプロンプトで次の内容を実行
```
./stop_server.sh
```

## このサーバーを使っているアプリケーション
- [susumu_ai_dialogue_system](https://github.com/sato-susumu/susumu_ai_dialogue_system)

## 謝辞
ネガポジではない、基本8感情を扱った貴重なデータセット「[WRIME: 主観と客観の感情分析データセット](https://github.com/ids-cv/wrime)」を作成し公開してくださった梶原 智之氏、中島 悠太氏に感謝致します。
