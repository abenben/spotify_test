# 「4/30(金)【第365回】オンラインもくもく会(夜)」での勉強

## 日時 

* 2021/4/30 21:00〜

## 勉強会のURL

* https://no-genre-mokumoku.connpass.com/event/211358/

## 勉強の目的（予定）

* Spotify APIをPythonから動かす（音楽を開始する）

## 成果

* https://github.com/abenben/spotify_test

## 何をしたか

### 1.情報を探す

* Webで情報検索
    * Spotifyのデベロッパーサイト ： https://developer.spotify.com/
         * プログラムから認証するために使うIDやシークレットキーが取得できる。
    * ライブラリ（spotify） ： https://github.com/plamere/spotipy
         * 数あるPythonのspotifyライブラリ中から人気の高そうなライブラリを発見
    * 技術ブログなど ： https://qiita.com/EkatoPgm/items/15f1a61bc2fe01c8a0c9
* はまりどころ
    * Spotifyで認証させる方法がよくわからなかった。結局、RedirectURLsに適当なURL（ http://localhost:8080 等)を入力すればいいだけだった。
    * Pythonにどんなライブラリがあるか"spotify"をキーワードに検索したところ、たくさんありすぎて、どれがおすすめか悩んだ。
    * spotipyとspotifyというライブラリがあり、最初間違ってspotifyをインストールした。

### 2.処理内容

* Spotify Web APIを使用して、ファイルに曲のURIが含まれるリストを読み込み、曲を再生します。
* 曲を再生する前に、曲の再生状態を取得し、曲が再生されるのを待ちます。
* 曲が終了するまで待ち、次の曲に進みます。

### 3.環境変数

* CLIENT_ID：Spotify Web APIにアクセスするためのクライアントID。
* CLIENT_SECRET：Spotify Web APIにアクセスするためのクライアントシークレット。
* REDIRECT_URI：Spotify Web APIで認証が完了した後に、ユーザーをリダイレクトするURI。

### 4.Spotifyの曲リスト

songs.txtファイルには、再生したいSpotifyの曲のURIを1行に1つずつ書き込みます。

```
https://open.spotify.com/track/79UdkvJdipN8pQEdRHu8zQ
https://open.spotify.com/track/336kKvuGSevWcIfpWUmwjl
https://open.spotify.com/track/4YMukCV1BsdK8V9kZoQpT6
```

### 5.実行方法

ターミナルで、python main.pyと入力して実行します。

```shell
$ python main.py
```
