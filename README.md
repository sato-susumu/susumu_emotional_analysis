## 概要
テキストを入力として受け取り、感情情報(喜び、悲しみ、期待、驚き、怒り、恐れ、嫌悪)を推定して返すサーバーです。
[WRIME: 主観と客観の感情分析データセット](https://github.com/ids-cv/wrime)でモデルを作り、 そのモデルをサーバーで利用しています。
<br/>
<br/>
<br/>


## 感情解析の例
| 入力                       | Joy  | Sadness | Anticipation | Surprise | Anger | Fear | Disgust | Trust |
| -------------------------- | ---- | ------- | ------------ | -------- | ----- | ---- | ------- | ----- |
| いいことあるかな           | 0.01 | 0.00    | 0.97         | 0.00     | 0.00  | 0.00 | 0.00    | 0.00  |
| おばけ怖い                 | 0.00 | 0.03    | 0.00         | 0.02     | 0.00  | 0.86 | 0.05    | 0.00  |
| ヤフオクで転売された。     | 0.19 | 0.24    | 0.10         | 0.36     | 0.00  | 0.04 | 0.02    | 0.00  |
| ヤッターヤッター大成功     | 0.95 | 0.00    | 0.00         | 0.01     | 0.00  | 0.00 | 0.00    | 0.01  |
| 俺、激おこ                 | 0.03 | 0.04    | 0.43         | 0.05     | 0.10  | 0.13 | 0.18    | 0.01  |
| じいちゃんが帰ってこない。 | 0.00 | 0.91    | 0.00         | 0.01     | 0.00  | 0.02 | 0.03    | 0.00  |
<br>

## 動作確認
Dockerが動く環境であれば、Windows, Linux, Macなどどの環境でも動作します。
<br/>
<br/>
<br/>


## 動作確認環境
Windows 11  
Ubuntu 22.04 on WSL
<br/>
<br/>
<br/>


## 使い方(Windows)
### 事前準備が必要なもの
Docker Desktop, gitのインストール

### ソースコード取得
コマンドラインで次の内容を実行
```
git clone https://github.com/sato-susumu/susumu_emotional_analysis.git
cd susumu_emotional_analysis
git lfs install
git lfs pull
```

### 起動
コマンドラインで次の内容を実行。初回などイメージのビルドが行われる場合は時間がかかります。サーバーの起動にも少し時間がかかります。
```
start_server.bat
```


### 停止
コマンドラインで次の内容を実行
```
stop_server.bat
```
<br/>
<br/>

## 使い方 (Ubuntu)

### 事前準備
git-lfsのインストール

### ソースコード取得
コマンドラインで次の内容を実行
```
git clone https://github.com/sato-susumu/susumu_emotional_analysis.git
cd susumu_emotional_analysis
git lfs install
git lfs pull
```

### 起動
コマンドプロンプトで次の内容を実行。初回などイメージのビルドが行われる場合は時間がかかります。サーバーの起動にも少し時間がかかります。
```
./start_server.sh
```

### 呼び出し例
コマンドプロンプトで次の内容を実行
```
curl -X POST -H "Content-Type: application/json" -d '{"text":"いい天気だ"}' http://127.0.0.1:56563/analyze_emotion
```

呼び出し結果
```
{"emotions":{"Joy":0.8913211822509766,"Sadness":0.0037260549142956734,"Anticipation":0.03549545258283615,"Surprise":0.03090864047408104,"Anger":0.000993472058326006,"Fear":0.002147842664271593,"Disgust":0.0024142847396433353,"Trust":0.03299309313297272}}
```

### 停止
コマンドプロンプトで次の内容を実行
```
./stop_server.sh
```
<br/>
<br/>

## このサーバーを使っているアプリケーション
- [susumu_ai_dialogue_system](https://github.com/sato-susumu/susumu_ai_dialogue_system)
<br/>

## 謝辞
ポジネガではない、基本8感情を扱った貴重なデータセット「[WRIME: 主観と客観の感情分析データセット](https://github.com/ids-cv/wrime)」を作成し公開してくださった梶原 智之さん、中島 悠太さんに感謝致します。Google Colaboratoryを使ってわかりやすくモデル作成方法を公開してくださった@izaki_shinさんに感謝いたします。
<br/>
