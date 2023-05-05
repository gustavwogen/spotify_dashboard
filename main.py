
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import streamlit as st

from spotify import create_client, create_tracks_df


def main():
    client = create_client()
    df = create_tracks_df(client)
    songs, artists, albums = df['track title'], ['artists'], df['album']
    # st.set_page_config(
    #     page_title="Spotify Dashboard",
    #     page_icon="🧊",
    #     layout="centered",
    #     initial_sidebar_state="auto",
    #     menu_items={
    #         'About': "# This is a header. This is an *extremely* cool app!"
    #     }
    # )
    st.title('Spotify Dashboard')
    col1, col2, col3 = st.columns(3)
    # st.table(data=df)



if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
