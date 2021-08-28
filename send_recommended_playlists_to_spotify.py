import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd

# Connect to Spotify Web API
spotify_json_file = 'spotify_data/spotify_credentials.json'
with open(spotify_json_file, 'r') as spotify_details:
    data = spotify_details.read()
spotify_details_dict = json.loads(data)
scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=spotify_details_dict['client_id'],
    client_secret=spotify_details_dict['client_secret'],
    redirect_uri=spotify_details_dict['redirect_uri'],
    scope=scope,
))
# Check
print(f'Current user --> {sp.current_user()["display_name"]}')

user_id = sp.current_user()['id']

# Create a new playlist for tracks to add
new_playlist = sp.user_playlist_create(user=user_id,
                                       name="K-Nearest Neighbours playlist",
                                       public=False,
                                       collaborative=False,
                                       description="Created by Veer Singh",
                                       )

# Add tracks to the new playlist
recommended_tracks_k_nearest_neighbours = pd.read_pickle(
    'recommended_track_ids/recommended_tracks_k_nearest_neighbours.pkl')
for track_id in recommended_tracks_k_nearest_neighbours:
    sp.user_playlist_add_tracks(user=user_id,
                                playlist_id=new_playlist['id'],
                                tracks=[track_id],
                                )

# Create a new playlist for tracks to add
new_playlist = sp.user_playlist_create(user=user_id,
                                       name="Random Forest playlist",
                                       public=False,
                                       collaborative=False,
                                       description="Created by Veer Singh",
                                       )

# Add tracks to the new playlist
recommended_tracks_random_forest = pd.read_pickle(
    'recommended_track_ids/recommended_tracks_random_forest.pkl')
for track_id in recommended_tracks_random_forest:
    sp.user_playlist_add_tracks(user=user_id,
                                playlist_id=new_playlist['id'],
                                tracks=[track_id],
                                )
