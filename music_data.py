from connect_to_api import connect_to_api
from helper_data_functions import get_top_artists_dataframe

# Connect to Spotify API
connection_details_json = 'spotify_data/veer_spotify_details.json'  # connection details json file
sp = connect_to_api(connection_details_json)

# Get top artists data
top_artists = sp.current_user_top_artists(limit=50)
top_artists_df = get_top_artists_dataframe(top_artists)