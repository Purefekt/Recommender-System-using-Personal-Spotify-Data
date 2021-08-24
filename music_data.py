from connect_to_api import connect_to_api
from helper_data_functions import get_top_tracks_ids_dataframe
from helper_data_functions import get_saved_tracks_ids_dataframe
from helper_data_functions import get_top_tracks_ids_of_top_artists_dataframe
from helper_data_functions import get_random_tracks_ids
from helper_data_functions import get_tracks_features
from helper_data_functions import get_recommended_tracks_dataframe


# Connect to Spotify API. Delete .cache file for new user's data
connection_details_json = 'spotify_data/spotify_credentials.json'
sp = connect_to_api(connection_details_json)

# Print current user
print(f'Current user --> {sp.current_user()["display_name"]}')

print("Getting and saving ids of user's top tracks...")
top_tracks_ids_df = get_top_tracks_ids_dataframe(sp=sp)
top_tracks_ids_df.to_csv('spotify_data/top_tracks_ids.csv')
top_tracks_ids_df.to_pickle('spotify_data/top_tracks_ids.pkl')

print("Getting and saving ids of user's saved tracks...")
saved_tracks_ids_df = get_saved_tracks_ids_dataframe(sp=sp)
saved_tracks_ids_df.to_csv('spotify_data/saved_tracks_ids.csv')
saved_tracks_ids_df.to_pickle('spotify_data/saved_tracks_ids.pkl')

print("Getting and saving ids of top 10 tracks of user's top artists...")
top_tracks_of_top_artists_df = get_top_tracks_ids_of_top_artists_dataframe(sp=sp)
top_tracks_of_top_artists_df.to_csv('spotify_data/top_tracks_of_top_artists.csv')
top_tracks_of_top_artists_df.to_pickle('spotify_data/top_tracks_of_top_artists.pkl')

print("Getting and saving ids of random tracks...")
random_tracks_ids_df = get_random_tracks_ids(sp=sp)
random_tracks_ids_df.to_csv('spotify_data/random_tracks_ids.csv')
random_tracks_ids_df.to_pickle('spotify_data/random_tracks_ids.pkl')

print("Getting and saving track features of top tracks , saved tracks, top artists tracks and random tracks...")
tracks_features_df = get_tracks_features(sp=sp)
tracks_features_df.to_csv('spotify_data/tracks_features.csv')
tracks_features_df.to_pickle('spotify_data/tracks_features.pkl')

print("Getting and saving track features of recommended tracks...")
recommended_tracks_df = get_recommended_tracks_dataframe(sp=sp)
recommended_tracks_df.to_csv('spotify_data/recommended_tracks.csv')
recommended_tracks_df.to_pickle('spotify_data/recommended_tracks.pkl')
