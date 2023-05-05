from unittest.mock import Mock, patch

import spotipy
import spotify


@patch("spotify.SpotifyOAuth")
@patch("spotify.spotipy")
def test_create_client(mock_spotipy, mock_oauth):
    mock_spotipy.Spotify.return_value = spotipy.client.Spotify
    mock_oauth.return_value = spotipy.oauth2.SpotifyOAuth

    spotify.create_client()

    mock_spotipy.Spotify.assert_called_once_with(auth_manager=mock_oauth())



def test_create_tracks_df():
    keys_in_res = ['items', 'total', 'limit', 'offset', 'href', 'next', 'previous']
    mock_client = Mock(name="client")
    mock_client.current_user_top_tracks.keys.return_value = keys_in_res
    
    