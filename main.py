import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

# Spotify APIのクライアントID、クライアントシークレット、リダイレクトURI
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')
redirect_uri = os.environ.get('REDIRECT_URI')

# Spotifyの認証を取得する
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri))

# 曲が保存されているファイルパス
songs_file = "songs.txt"

# 曲を再生する関数
def play_songs(songs_file):
    with open(songs_file, "r") as f:
        song_list = f.readlines()

    # 曲を再生する
    for song_uri in song_list:
        song_uri = song_uri.strip() # 改行を削除する
        print(f"Now playing: {song_uri}")
        sp.start_playback(uris=[song_uri])
        # 曲の再生状態を取得する
        playback_state = sp.current_playback()
        while playback_state is not None and not playback_state['is_playing']:
            time.sleep(1)
            playback_state = sp.current_playback()
        # 曲が終了するまで待つ
        while playback_state is not None and playback_state['is_playing']:
            time.sleep(1)
            playback_state = sp.current_playback()

if __name__ == "__main__":
    play_songs(songs_file)
