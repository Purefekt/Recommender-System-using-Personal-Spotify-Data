import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Connect to the Spotify API
with open('veer_spotify_details.json', 'r') as spotify_details:
    data=spotify_details.read()
spotify_details_dict = json.loads(data)

# https://developer.spotify.com/web-api/using-scopes/
scope = "user-library-read user-follow-read user-top-read playlist-read-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=spotify_details_dict['client_id'],
    client_secret=spotify_details_dict['client_secret'],
    redirect_uri=spotify_details_dict['redirect_uri'],
    scope=scope,
))


