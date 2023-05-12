import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

from pprint import pprint


def create_client():
    scope = "user-top-read"
    client = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    return client


def create_top_tracks_df(
    client: spotipy.client.Spotify, limit=50, offset=0, time_range="medium_term"
):
    results = client.current_user_top_tracks(limit, offset, time_range)
    table = []
    for item in results["items"]:
        row = {}
        album_title = item["album"]["name"]
        large_img, medium_img, small_img = item["album"]["images"][:3]
        track_title = item["name"]
        track_url = item["external_urls"]["spotify"]
        artists = [artist["name"] for artist in item["artists"]]

        row["album"] = album_title
        row["artists"] = ", ".join(artists)
        row["track title"] = track_title
        row["track url"] = track_url
        row["album cover large"] = large_img["url"]
        row["album cover medium"] = medium_img["url"]
        row["album cover small"] = small_img["url"]
        table.append(row)
    df = pd.DataFrame.from_records(table)
    return df


def create_top_artists_df(
    client: spotipy.client.Spotify, limit=50, offset=0, time_range="medium_term"
):
    results = client.current_user_top_artists(limit, offset, time_range)
    table = []
    for item in results["items"]:
        pprint(item)
        row = {}
        if len(item["images"]):
            pprint(item)
        large_img, medium_img, small_img = item["images"][:3]

        row["name"] = item["name"]
        row["popularity"] = item["popularity"]
        row["artist url"] = item["external_urls"]["spotify"]
        row["artist cover small"] = small_img["url"]
        row["artist cover medium"] = medium_img["url"]
        row["artist cover large"] = large_img["url"]

        table.append(row)
    df = pd.DataFrame.from_records(table)
    return df
