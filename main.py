# osモジュールをインポート
import os
# spotipyパッケージをインポート
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# 環境変数からクライアントID、クライアントシークレット、リダイレクトURIを取得
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
redirect_uri = os.environ.get("REDIRECT_URI")

# 曲を表示するための関数を定義
def show_tracks(results):
    for i, item in enumerate(results["items"]):
        track = item["track"]
        print("   %d %32.32s %s¥n" % (i, track["artists"][0]["name"], track["name"]))


if __name__ == "__main__":

    # SpotifyOAuthオブジェクトを使用して、SpotifyAPIに認証されたSpotipyオブジェクトを作成
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope="user-read-playback-state,user-modify-playback-state",
        )
    )

    # ユーザーのSpotifyデバイスのリストを取得し、アクティブなデバイスを見つける
    devices = sp.devices()
    active_device: None = next(
        (device for device in devices["devices"] if device["is_active"]), None
    )
    # アクティブなデバイスが見つかった場合は、そのデバイスで曲を再生する
    if active_device:
        print("Active device found: {}".format(active_device["name"]))
        sp.start_playback(device_id=active_device["id"], uris=["spotify:track:2AVbKUuvvzbPK6NIZZZvcY"])
    else:
        print("No active device found.")

    # ユーザーのプレイリストのリストを取得し、プレイリストごとに曲を表示する
    playlists = sp.current_user_playlists()
    user_id = sp.me()["id"]

    for playlist in playlists["items"]:
        if playlist["owner"]["id"] == user_id:
            print("%s¥n" % playlist["name"])
            print(f"  total tracks {playlist['tracks']['total']}¥n")

            results = sp.playlist(playlist["id"], fields="tracks,next")
            tracks = results["tracks"]
            show_tracks(tracks)

            while tracks["next"]:
                tracks = sp.next(tracks)
                show_tracks(tracks)

            # 指定されたトラックを再生する
            sp.start_playback(uris=["spotify:track:2AVbKUuvvzbPK6NIZZZvcY"])
            break

    # 最後に指定されたトラックを再生する
    sp.start_playback(uris=["spotify:track:2AVbKUuvvzbPK6NIZZZvcY"])
