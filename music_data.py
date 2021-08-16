from connect_to_api import connect_to_api
from helper_data_functions import get_top_artists_dataframe
from helper_data_functions import get_followed_artists_dataframe
from helper_data_functions import get_top_tracks_dataframe
from helper_data_functions import get_saved_tracks_dataframe
from helper_data_functions import get_playlist_tracks_dataframe
from helper_data_functions import get_recommendation_track_dataframe

# Connect to Spotify API. Delete .cache file for new user's data
connection_details_json = 'spotify_data/apu_spotify_details.json'
sp = connect_to_api(connection_details_json)

# debug
# print(sp.current_user()['display_name'])
# df.to_csv('file_name.csv')

# # Get top artists data
top_artists_df = get_top_artists_dataframe(sp=sp)

# # Get followed artists data
followed_artists_df = get_followed_artists_dataframe(sp=sp)
#
# # Get top tracks data
top_tracks_df = get_top_tracks_dataframe(sp=sp)

# # Get saved tracks data
saved_tracks_df = get_saved_tracks_dataframe(sp=sp)

# # Get playlists tracks data
playlist_tracks_df = get_playlist_tracks_dataframe(sp=sp)

# Get recommendation tracks from some sample top playlists
recommendation_tracks_df = get_recommendation_track_dataframe(sp=sp)
