from unittest.mock import Mock, patch
import json

from spotipy.oauth2 import SpotifyOAuth
import spotify


@patch("spotify.SpotifyOAuth")
@patch("spotify.spotipy")
def test_create_client(mock_spotipy, mock_oauth):
    scope = "user-top-read"
    mock_spotipy.Spotify.return_value = Mock(name="client")
    mock_oauth.return_value = Mock(name="SpotifyOAuth")

    spotify.create_client()

    mock_oauth.assert_called_once_with(scope=scope)
    mock_spotipy.Spotify.assert_called_once_with(auth_manager=mock_oauth())


@patch("spotify.pd")
def test_create_top_tracks_df(mock_pd):
    mock_client = Mock(name="client")
    LIMIT = 50
    with open("tests/responses/tracks.json") as f:
        sample_response = json.load(f)

    mock_client.current_user_top_tracks.return_value = sample_response

    mock_df = Mock(name="mock_dataframe")
    mock_pd.DataFrame.from_records.return_value = mock_df

    spotify.create_top_tracks_df(mock_client)
