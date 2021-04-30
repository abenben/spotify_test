# 「4/30(金)【第365回】オンラインもくもく会(夜)」での勉強

## 日時 

* 2021/4/30 21:00〜

## 勉強会のURL

* https://no-genre-mokumoku.connpass.com/event/211358/

## 勉強の目的（予定）

* Spotify APIをPythonから動かす（音楽を開始する）

## 成果

* このGitHubにアップロードした

## 何をしたか

### 1.情報を探す

* Webで検索
    * Spotifyのデベロッパーサイト ： https://developer.spotify.com/
    * ライブラリ（spotify） ： https://github.com/plamere/spotipy
    * ブログなど ： https://qiita.com/EkatoPgm/items/15f1a61bc2fe01c8a0c9
* はまりどころ
    * Spotifyで認証させる方法がよくわからなかった。結局、RedirectURLsに適当なURL（http://localhost:8080等）を入力すればいいだけだった。
    * Pythonにどんなライブラリがあるか"spotify"をキーワードに検索したところ、たくさんありすぎて、どれがおすすめか悩んだ
    * spotypyとspotifyというライブラリがあり、最初間違ってspotifyをインストールした

### 2.動作確認

* とりあえず認証を行い。
* サンプルを実行
* デバイスとかプレイリストの動作確認

### 3.目的を果たす

* プレイリストを一覧表示したり、何か音楽を演奏させた。

### 4.できなかったこと

* Spotypyを立ち上げただけだと演奏できなかったので後で調べる。何か演奏した後だと問題なく好きな曲へ切り替え演奏ができる。