import os
import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
redirect_uri = os.environ.get("REDIRECT_URI")


def show_tracks(results):
    for i, item in enumerate(results["items"]):
        track = item["track"]
        print("   %d %32.32s %s¥n" % (i, track["artists"][0]["name"], track["name"]))


if __name__ == "__main__":

    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope="user-read-playback-state,user-modify-playback-state",
        )
    )

    res = sp.devices()
    print(json.dumps(res, indent=2))

    # playlists = sp.current_user_playlists()
    # user_id = sp.me()["id"]
    #
    # for playlist in playlists["items"]:
    #     if playlist["owner"]["id"] == user_id:
    #         print("%s¥n" % playlist["name"])
    #         print("  total tracks %s¥n" % playlist["tracks"]["total"])
    #
    #         results = sp.playlist(playlist["id"], fields="tracks,next")
    #         tracks = results["tracks"]
    #         show_tracks(tracks)
    #
    #         while tracks["next"]:
    #             tracks = sp.next(tracks)
    #             show_tracks(tracks)

    sp.start_playback(uris=["spotify:track:2AVbKUuvvzbPK6NIZZZvcY"])
