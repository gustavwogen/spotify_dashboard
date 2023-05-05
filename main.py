
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
from pprint import pprint
import streamlit as st

from spotify import create_tracks_df


def main():
    scope = "user-top-read"
    client = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    df = create_tracks_df(client)
    print(df)
    print(os.environ)
    st.title('Uber pickups in NYC')


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
