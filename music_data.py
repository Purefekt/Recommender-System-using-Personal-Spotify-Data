from connect_to_api import connect_to_api
from helper_data_functions import get_top_artists_dataframe
from helper_data_functions import get_followed_artists_dataframe
from helper_data_functions import get_top_tracks_dataframe
from helper_data_functions import get_saved_tracks_dataframe
from helper_data_functions import get_playlist_tracks_dataframe
from helper_data_functions import get_recommendation_track_dataframe

# Connect to Spotify API. Delete .cache file for new user's data
connection_details_json = 'spotify_data/spotify_credentials.json'
sp = connect_to_api(connection_details_json)

# Print current user
print(f'Current user --> {sp.current_user()["display_name"]}')

# Get top artists data
print("Getting and saving current user's top artists data...")
top_artists_df = get_top_artists_dataframe(sp=sp)
top_artists_df.to_csv('spotify_data/top_artists.csv')
top_artists_df.to_pickle('spotify_data/top_artists.pkl')

# Get followed artists data
print("Getting and saving current user's followed artists data...")
followed_artists_df = get_followed_artists_dataframe(sp=sp)
followed_artists_df.to_csv('spotify_data/followed_artists.csv')
followed_artists_df.to_pickle('spotify_data/followed_artists.pkl')

# Get top tracks data
print("Getting and saving current user's top tracks data...")
top_tracks_df = get_top_tracks_dataframe(sp=sp)
top_tracks_df.to_csv('spotify_data/top_tracks.csv')
top_tracks_df.to_pickle('spotify_data/top_tracks.pkl')

# Get saved tracks data
print("Getting and saving current user's saved tracks data...")
saved_tracks_df = get_saved_tracks_dataframe(sp=sp)
saved_tracks_df.to_csv('spotify_data/saved_tracks.csv')
saved_tracks_df.to_pickle('spotify_data/saved_tracks.pkl')

# Get playlists tracks data
print("Getting and saving current user's playlists' tracks data...")
playlist_tracks_df = get_playlist_tracks_dataframe(sp=sp)
playlist_tracks_df.to_csv('spotify_data/playlist_tracks.csv')
playlist_tracks_df.to_pickle('spotify_data/playlist_tracks.pkl')

# Get recommended tracks from user's top tracks
print("Getting and saving current user's recommended tracks from top tracks...")
recommendation_tracks_df = get_recommendation_track_dataframe(sp=sp)
recommendation_tracks_df.to_csv('spotify_data/recommended_tracks.csv')
recommendation_tracks_df.to_pickle('spotify_data/recommended_tracks.pkl')
