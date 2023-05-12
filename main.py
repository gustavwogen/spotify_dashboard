import os
import logging
from spotipy.oauth2 import SpotifyOAuth
import streamlit as st

from spotify import create_client, create_top_tracks_df, create_top_artists_df

logger = logging.getLogger(__name__)
logger.setLevel(10)


def main():
    st.title("Spotify Dashboard")
    logger.info("hello this is from the logger")
    col1, col2 = st.columns(2)
    button_clicked = "songs"
    with col1:
        song_button = st.button("Top Songs")
    with col2:
        artist_button = st.button("Top Artists")

    client = create_client()
    if song_button:
        button_clicked = "songs"
        df = create_top_tracks_df(client)
        df
    elif artist_button:
        button_clicked = "artists"
        df = create_top_artists_df(client)
        df

    print("button clicked:", button_clicked)
    # st.set_page_config(
    #     page_title="Spotify Dashboard",
    #     page_icon="🧊",
    #     layout="centered",
    #     initial_sidebar_state="auto",
    #     menu_items={
    #         'About': "# This is a header. This is an *extremely* cool app!"
    #     }
    # )
    # st.table(data=df)


if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
