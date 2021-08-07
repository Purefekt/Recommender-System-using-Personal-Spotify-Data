from connect_to_api import connect_to_api
from helper_data_functions import  get_top_artists_unlimited
from helper_data_functions import get_top_artists_dataframe
from helper_data_functions import get_followed_artists_unlimited
from helper_data_functions import get_followed_artists_dataframe
from helper_data_functions import get_top_tracks_unlimited
from helper_data_functions import get_top_tracks_df

# Connect to Spotify API. Delete .cache file for new user's data
connection_details_json = 'spotify_data/apu_spotify_details.json'
sp = connect_to_api(connection_details_json)

# debug
# print(sp.current_user()['display_name'])
# df.to_csv('file_name.csv')

# Get top artists data
top_artists_list = get_top_artists_unlimited(sp, sp.current_user_top_artists())
top_artists_df = get_top_artists_dataframe(top_artists_list)

# Get followed artists data
followed_artists_list = get_followed_artists_unlimited(sp, sp.current_user_followed_artists())
followed_artists_df = get_followed_artists_dataframe(followed_artists_list)

# Get top tracks data
top_tracks_list = get_top_tracks_unlimited(sp, sp.current_user_top_tracks())
top_tracks_df = get_top_tracks_df(top_tracks_list)
