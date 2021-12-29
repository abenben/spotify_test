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

* Webで情報検索
    * Spotifyのデベロッパーサイト ： https://developer.spotify.com/
         * プログラムから認証するために使うIDやシークレットキーが取得できる。
    * ライブラリ（spotify） ： https://github.com/plamere/spotipy
         * 数あるPythonのspotifyライブラリ中から人気の高そうなライブラリを発見
    * 技術ブログなど ： https://qiita.com/EkatoPgm/items/15f1a61bc2fe01c8a0c9
* はまりどころ
    * Spotifyで認証させる方法がよくわからなかった。結局、RedirectURLsに適当なURL（http://localhost:8080等)を入力すればいいだけだった。
    * Pythonにどんなライブラリがあるか"spotify"をキーワードに検索したところ、たくさんありすぎて、どれがおすすめか悩んだ。
    * spotipyとspotifyというライブラリがあり、最初間違ってspotifyをインストールした。

### 2.動作確認

* とりあえず認証を行う。
* Web上のサンプルを実行する。
* 曲の演奏やデバイスとかプレイリストの動作を確認する。

### 3.目的を果たす

* プレイリストを一覧表示したり、好きな曲を演奏した。

### 4.今回できなかったこと

* Spotypyを立ち上げただけだと演奏できなかったので後で調べる。何か演奏した後だと問題なく好きな曲へ切り替え演奏ができる。
