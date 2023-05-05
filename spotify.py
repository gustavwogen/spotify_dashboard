import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth


def create_client():
    scope = "user-top-read"
    client = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    return client


def create_tracks_df(client: spotipy.client.Spotify, limit=50, offset=0, time_range='medium_term'):
    results = client.current_user_top_tracks(limit, offset, time_range)
    print(results)
    table = []
    for item in results['items']:
        row = {}
        album_title = item['album']['name']
        large_img, medium_img, small_img = item['album']['images']
        track_title = item['name']
        track_url = item['external_urls']['spotify']
        artists = [artist['name'] for artist in item['artists']]

        row['album'] = album_title
        row['artists'] = ", ".join(artists)
        row['track title'] = track_title
        row['track url'] = track_url
        row['album cover large'] = large_img['url']
        row['album cover medium'] = medium_img['url']
        row['album cover small'] = small_img['url']
        table.append(row)
    df = pd.DataFrame.from_records(table)
    return df
