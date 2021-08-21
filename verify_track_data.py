from connect_to_api import connect_to_api
connection_details_json = 'spotify_data/spotify_credentials.json'
sp = connect_to_api(connection_details_json)

# test if data of a track is legit
test_track_id = '30KctD1WsHKTIYczXjip5a'

track_name = sp.track(test_track_id)['name']
popularity = sp.track(test_track_id)['popularity']
track_type = sp.track(test_track_id)['type']
is_local = sp.track(test_track_id)['is_local']
explicit = sp.track(test_track_id)['explicit']
duration_ms = sp.track(test_track_id)['duration_ms']
disc_number = sp.track(test_track_id)['disc_number']
track_number = sp.track(test_track_id)['track_number']

artists_id = sp.track(test_track_id)['artists'][0]['id']
artists_name = sp.track(test_track_id)['artists'][0]['name']

album_artist_id = sp.track(test_track_id)['album']['artists'][0]['id']
album_artist_name = sp.track(test_track_id)['album']['artists'][0]['name']
album_id = sp.track(test_track_id)['album']['id']
album_name = sp.track(test_track_id)['album']['name']
album_release_date = sp.track(test_track_id)['album']['release_date']
album_tracks = sp.track(test_track_id)['album']['total_tracks']
album_type = sp.track(test_track_id)['album']['type']

# Audio features
danceability = sp.audio_features(test_track_id)[0]['danceability']
energy = sp.audio_features(test_track_id)[0]['energy']
track_key = sp.audio_features(test_track_id)[0]['key']
loudness = sp.audio_features(test_track_id)[0]['loudness']
mode = sp.audio_features(test_track_id)[0]['mode']
speechiness = sp.audio_features(test_track_id)[0]['speechiness']
acousticness = sp.audio_features(test_track_id)[0]['acousticness']
instrumentalness = sp.audio_features(test_track_id)[0]['instrumentalness']
liveness = sp.audio_features(test_track_id)[0]['liveness']
valence = sp.audio_features(test_track_id)[0]['valence']
tempo = sp.audio_features(test_track_id)[0]['tempo']
uri = sp.audio_features(test_track_id)[0]['uri']
track_href = sp.audio_features(test_track_id)[0]['track_href']
analysis_url = sp.audio_features(test_track_id)[0]['analysis_url']
time_signature = sp.audio_features(test_track_id)[0]['time_signature']


print(track_name, popularity, track_type, is_local, explicit, duration_ms, disc_number, track_number)
print(artists_id, artists_name)
print(album_artist_id, album_artist_name, album_id, album_name, album_release_date, album_tracks, album_type)
print(danceability, energy, track_key, loudness, mode, speechiness, acousticness, instrumentalness, liveness,
      valence, tempo, uri, track_href, analysis_url, time_signature)