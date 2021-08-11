import pandas as pd
import yaml


def get_top_artists_dataframe(sp):
    results = sp.current_user_top_artists()
    top_artists_list = results['items']
    while results['next']:
        results = sp.next(results)
        top_artists_list.extend(results['items'])

    artist_id, uri, artist_type, name, genres, followers = list(), list(), list(), list(), list(), list()

    for i in range(len(top_artists_list)):

        # Status
        print(f'{int((i / len(top_artists_list)) * 100)}% done...')

        artist_id.append(top_artists_list[i]['id'])
        uri.append(top_artists_list[i]['uri'])
        artist_type.append(top_artists_list[i]['type'])
        name.append(top_artists_list[i]['name'])
        genres.append(top_artists_list[i]['genres'])
        followers.append(top_artists_list[i]['followers']['total'])

    top_artists_dict = {'id': artist_id,
                        'uri': uri,
                        'type': artist_type,
                        'name': name,
                        'genres': genres,
                        'followers': followers
                        }

    top_artists_df = pd.DataFrame(data=top_artists_dict)
    return top_artists_df


def get_followed_artists_dataframe(sp):
    results = sp.current_user_followed_artists()
    followed_artists_list = results['artists']['items']
    while results['artists']['next']:
        results = sp.next(results['artists'])
        followed_artists_list.extend(results['artists']['items'])

    artist_id, uri, artist_type, name, genres, followers = list(), list(), list(), list(), list(), list(),

    for i in range(len(followed_artists_list)):

        # Status
        print(f'{int((i / len(followed_artists_list)) * 100)}% done...')

        artist_id.append(followed_artists_list[i]['id'])
        uri.append(followed_artists_list[i]['uri'])
        artist_type.append(followed_artists_list[i]['type'])
        name.append(followed_artists_list[i]['name'])
        genres.append(followed_artists_list[i]['genres'])
        followers.append(followed_artists_list[i]['followers']['total'])

    followed_artists_dict = {'id': artist_id,
                             'uri': uri,
                             'type': artist_type,
                             'name': name,
                             'genres': genres,
                             'followers': followers
                             }

    followed_artists_df = pd.DataFrame(data=followed_artists_dict)
    return followed_artists_df


def get_top_tracks_dataframe(sp):
    results = sp.current_user_top_tracks()
    top_tracks_list = results['items']
    while results['next']:
        results = sp.next(results)
        top_tracks_list.extend(results['items'])

    # 18 cols for tracks data
    track_id, name, popularity, track_type, is_local, explicit, duration_ms, disc_number, track_number, artist_id, \
    artist_name, album_artist_id, album_artist_name, album_id, album_name, album_release_date, album_tracks, \
    album_type = list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), \
                 list(), list(), list(), list(), list(), list(),

    # 17 cols for track audio features
    genres_artist, album_genres, danceability, energy, track_key, loudness, mode, speechiness, acousticness, \
    instrumentalness, liveness, valence, tempo, uri, track_href, analysis_url, \
    time_signature = list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), \
                     list(), list(), list(), list(), list(),

    for i in range(len(top_tracks_list)):

        # Status
        print(f'{int((i / len(top_tracks_list)) * 100)}% done...')

        # Tracks
        track_id.append(top_tracks_list[i]['id'])
        name.append(top_tracks_list[i]['name'])
        popularity.append(top_tracks_list[i]['popularity'])
        track_type.append(top_tracks_list[i]['type'])
        is_local.append(top_tracks_list[i]['is_local'])
        explicit.append(top_tracks_list[i]['explicit'])
        duration_ms.append(top_tracks_list[i]['duration_ms'])
        disc_number.append(top_tracks_list[i]['disc_number'])
        track_number.append(top_tracks_list[i]['track_number'])
        artist_id.append(top_tracks_list[i]['artists'][0]['id'])
        artist_name.append(top_tracks_list[i]['artists'][0]['name'])
        album_artist_id.append(top_tracks_list[i]['album']['artists'][0]['id'])
        album_artist_name.append(top_tracks_list[i]['album']['artists'][0]['name'])
        album_id.append(top_tracks_list[i]['album']['id'])
        album_name.append(top_tracks_list[i]['album']['name'])
        album_release_date.append(top_tracks_list[i]['album']['release_date'])
        album_tracks.append(top_tracks_list[i]['album']['total_tracks'])
        album_type.append(top_tracks_list[i]['album']['type'])

        # Track audio features
        genres_artist.append(sp.artists({artist_id[i]})['artists'][0]['genres'])
        album_genres.append(sp.artists({album_artist_id[i]})['artists'][0]['genres'])
        danceability.append(sp.audio_features(track_id[i])[0]['danceability'])
        energy.append(sp.audio_features(track_id[i])[0]['energy'])
        track_key.append(sp.audio_features(track_id[i])[0]['key'])
        loudness.append(sp.audio_features(track_id[i])[0]['loudness'])
        mode.append(sp.audio_features(track_id[i])[0]['mode'])
        speechiness.append(sp.audio_features(track_id[i])[0]['speechiness'])
        acousticness.append(sp.audio_features(track_id[i])[0]['acousticness'])
        instrumentalness.append(sp.audio_features(track_id[i])[0]['instrumentalness'])
        liveness.append(sp.audio_features(track_id[i])[0]['liveness'])
        valence.append(sp.audio_features(track_id[i])[0]['valence'])
        tempo.append(sp.audio_features(track_id[i])[0]['tempo'])
        uri.append(sp.audio_features(track_id[i])[0]['uri'])
        track_href.append(sp.audio_features(track_id[i])[0]['track_href'])
        analysis_url.append(sp.audio_features(track_id[i])[0]['analysis_url'])
        time_signature.append(sp.audio_features(track_id[i])[0]['time_signature'])

    top_tracks_dict = {'id': track_id,
                       'name': name,
                       'popularity': popularity,
                       'type': track_type,
                       'is_local': is_local,
                       'explicit': explicit,
                       'duration_ms': duration_ms,
                       'disc_number': disc_number,
                       'track_number': track_number,
                       'artist_id': artist_id,
                       'artist_name': artist_name,
                       'album_artist_id': album_artist_id,
                       'album_artist_name': album_artist_name,
                       'album_id': album_id,
                       'album_name': album_name,
                       'album_release_date': album_release_date,
                       'album_tracks': album_tracks,
                       'album_type': album_type,
                       'genres': genres_artist,
                       'album_genres': album_genres,
                       'danceability': danceability,
                       'energy': energy,
                       'key': track_key,
                       'loudness': loudness,
                       'mode': mode,
                       'speechiness': speechiness,
                       'acousticness': acousticness,
                       'instrumentalness': instrumentalness,
                       'liveness': liveness,
                       'valence': valence,
                       'tempo': tempo,
                       'uri': uri,
                       'track_href': track_href,
                       'analysis_url': analysis_url,
                       'time_signature': time_signature
                       }

    top_tracks_df = pd.DataFrame(data=top_tracks_dict)
    return top_tracks_df


def get_saved_tracks_dataframe(sp):
    results = sp.current_user_saved_tracks()
    saved_tracks_list = results['items']
    while results['next']:
        results = sp.next(results)
        saved_tracks_list.extend(results['items'])

    # 19 cols for tracks
    track_id, name, popularity, track_type, is_local, explicit, duration_ms, disc_number, track_number, artist_id, \
    artist_name, album_artist_id, album_artist_name, album_id, album_name, album_release_date, album_tracks, \
    album_type, added_at = list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), \
                           list(), list(), list(), list(), list(), list(), list(), list()

    # 17 cols for audio features
    genres_artist, album_genres, danceability, energy, track_key, loudness, mode, speechiness, acousticness, \
    instrumentalness, liveness, valence, tempo, uri, track_href, analysis_url, \
    time_signature = list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), \
                     list(), list(), list(), list(), list(),

    for i in range(len(saved_tracks_list)):

        # Status
        print(f'{int((i / len(saved_tracks_list)) * 100)}% done...')

        # Tracks
        track_id.append(saved_tracks_list[i]['track']['id'])
        name.append(saved_tracks_list[i]['track']['name'])
        popularity.append(saved_tracks_list[i]['track']['popularity'])
        track_type.append(saved_tracks_list[i]['track']['type'])
        is_local.append(saved_tracks_list[i]['track']['is_local'])
        explicit.append(saved_tracks_list[i]['track']['explicit'])
        duration_ms.append(saved_tracks_list[i]['track']['duration_ms'])
        disc_number.append(saved_tracks_list[i]['track']['disc_number'])
        track_number.append(saved_tracks_list[i]['track']['track_number'])
        artist_id.append(saved_tracks_list[i]['track']['artists'][0]['id'])
        artist_name.append(saved_tracks_list[i]['track']['artists'][0]['name'])
        album_artist_id.append(saved_tracks_list[i]['track']['album']['artists'][0]['id'])
        album_artist_name.append(saved_tracks_list[i]['track']['album']['artists'][0]['name'])
        album_id.append(saved_tracks_list[i]['track']['album']['id'])
        album_name.append(saved_tracks_list[i]['track']['album']['name'])
        album_release_date.append(saved_tracks_list[i]['track']['album']['release_date'])
        album_tracks.append(saved_tracks_list[i]['track']['album']['total_tracks'])
        album_type.append(saved_tracks_list[i]['track']['album']['type'])
        added_at.append(saved_tracks_list[i]['added_at'])

        # Track audio features
        genres_artist.append(sp.artists({artist_id[i]})['artists'][0]['genres'])
        album_genres.append(sp.artists({album_artist_id[i]})['artists'][0]['genres'])
        danceability.append(sp.audio_features(track_id[i])[0]['danceability'])
        energy.append(sp.audio_features(track_id[i])[0]['energy'])
        track_key.append(sp.audio_features(track_id[i])[0]['key'])
        loudness.append(sp.audio_features(track_id[i])[0]['loudness'])
        mode.append(sp.audio_features(track_id[i])[0]['mode'])
        speechiness.append(sp.audio_features(track_id[i])[0]['speechiness'])
        acousticness.append(sp.audio_features(track_id[i])[0]['acousticness'])
        instrumentalness.append(sp.audio_features(track_id[i])[0]['instrumentalness'])
        liveness.append(sp.audio_features(track_id[i])[0]['liveness'])
        valence.append(sp.audio_features(track_id[i])[0]['valence'])
        tempo.append(sp.audio_features(track_id[i])[0]['tempo'])
        uri.append(sp.audio_features(track_id[i])[0]['uri'])
        track_href.append(sp.audio_features(track_id[i])[0]['track_href'])
        analysis_url.append(sp.audio_features(track_id[i])[0]['analysis_url'])
        time_signature.append(sp.audio_features(track_id[i])[0]['time_signature'])

    saved_tracks_dict = {'id': track_id,
                         'name': name,
                         'popularity': popularity,
                         'type': track_type,
                         'is_local': is_local,
                         'explicit': explicit,
                         'duration_ms': duration_ms,
                         'disc_number': disc_number,
                         'track_number': track_number,
                         'artist_id': artist_id,
                         'artist_name': artist_name,
                         'album_artist_id': album_artist_id,
                         'album_artist_name': album_artist_name,
                         'album_id': album_id,
                         'album_name': album_name,
                         'album_release_date': album_release_date,
                         'album_tracks': album_tracks,
                         'album_type': album_type,
                         'added_at': added_at,
                         'genres': genres_artist,
                         'album_genres': album_genres,
                         'danceability': danceability,
                         'energy': energy,
                         'key': track_key,
                         'loudness': loudness,
                         'mode': mode,
                         'speechiness': speechiness,
                         'acousticness': acousticness,
                         'instrumentalness': instrumentalness,
                         'liveness': liveness,
                         'valence': valence,
                         'tempo': tempo,
                         'uri': uri,
                         'track_href': track_href,
                         'analysis_url': analysis_url,
                         'time_signature': time_signature
                         }

    saved_tracks_df = pd.DataFrame(data=saved_tracks_dict)
    return saved_tracks_df


def get_playlist_tracks_dataframe(sp):
    # limiting this to 50 playlists to avoid too much data
    playlists = sp.current_user_playlists()
    playlists = playlists['items']

    # 18 cols for tracks details
    track_id, name, popularity, track_type, is_local, explicit, duration_ms, disc_number, track_number, artist_id, \
    artist_name, album_artist_id, album_artist_name, album_id, album_name, album_release_date, album_tracks, \
    album_type = list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), \
                 list(), list(), list(), list(), list(), list()

    # 5 cols for playlist details
    playlist_id, playlist_name, no_of_tracks_in_playlist, added_at, added_by = list(), list(), list(), list(), list()

    # 17 cols for audio features
    genres_artist, album_genres, danceability, energy, track_key, loudness, mode, speechiness, acousticness, \
    instrumentalness, liveness, valence, tempo, uri, track_href, analysis_url, time_signature = \
        list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), \
        list(), list(), list(), list()

    # Get playlist id one by one
    for i in range(len(playlists)):
        # Skip broken album
        if sp.playlist_tracks(playlists[i]['id'])['items'][1]['track'] is None:
            print('Skipped an album')
            i = i + 1

        # Data used for 3 playlist columns
        current_playlist_id = playlists[i]['id']
        current_playlist_name = playlists[i]['name']
        no_of_tracks_in_current_playlist = sp.playlist_tracks(current_playlist_id)['total']

        # To get all the tracks in the playlist
        results = sp.playlist_tracks(current_playlist_id)
        tracks_in_playlist_list = results['items']
        while results['next']:
            results = sp.next(results)
            tracks_in_playlist_list.extend(results['items'])

        # Status
        print(f'{int((i / len(playlists)) * 100)}% done...')

        for j in range(no_of_tracks_in_current_playlist):
            # Tracks
            track_id.append(tracks_in_playlist_list[j]['track']['id'])
            name.append(tracks_in_playlist_list[j]['track']['name'])
            popularity.append(tracks_in_playlist_list[j]['track']['popularity'])
            track_type.append(tracks_in_playlist_list[j]['track']['type'])
            is_local.append(tracks_in_playlist_list[j]['track']['is_local'])
            explicit.append(tracks_in_playlist_list[j]['track']['explicit'])
            duration_ms.append(tracks_in_playlist_list[j]['track']['duration_ms'])
            disc_number.append(tracks_in_playlist_list[j]['track']['disc_number'])
            track_number.append(tracks_in_playlist_list[j]['track']['track_number'])
            artist_id.append(tracks_in_playlist_list[j]['track']['artists'][0]['id'])
            artist_name.append(tracks_in_playlist_list[j]['track']['artists'][0]['name'])
            album_artist_id.append(tracks_in_playlist_list[j]['track']['album']['artists'][0]['id'])
            album_artist_name.append(tracks_in_playlist_list[j]['track']['album']['artists'][0]['name'])
            album_id.append(tracks_in_playlist_list[j]['track']['album']['id'])
            album_name.append(tracks_in_playlist_list[j]['track']['album']['name'])
            album_release_date.append(tracks_in_playlist_list[j]['track']['album']['release_date'])
            album_tracks.append(tracks_in_playlist_list[j]['track']['album']['total_tracks'])
            album_type.append(tracks_in_playlist_list[j]['track']['album']['type'])

            # Playlists
            playlist_id.append(current_playlist_id)
            playlist_name.append(current_playlist_name)
            no_of_tracks_in_playlist.append(no_of_tracks_in_current_playlist)
            added_at.append(tracks_in_playlist_list[j]['added_at'])
            added_by.append(tracks_in_playlist_list[j]['added_by'])

            # Track audio features
            genres_artist.append(sp.artist(tracks_in_playlist_list[j]['track']['artists'][0]['id'])['genres'])
            album_genres.append(sp.artist(tracks_in_playlist_list[j]['track']['album']['artists'][0]['id'])['genres'])
            danceability.append(sp.audio_features(tracks_in_playlist_list[j]['track']['id'])[0]['danceability'])
            energy.append(sp.audio_features(tracks_in_playlist_list[j]['track']['id'])[0]['energy'])
            track_key.append(sp.audio_features(tracks_in_playlist_list[j]['track']['id'])[0]['key'])
            loudness.append(sp.audio_features(tracks_in_playlist_list[j]['track']['id'])[0]['loudness'])
            mode.append(sp.audio_features(tracks_in_playlist_list[j]['track']['id'])[0]['mode'])
            speechiness.append(sp.audio_features(tracks_in_playlist_list[j]['track']['id'])[0]['speechiness'])
            acousticness.append(sp.audio_features(tracks_in_playlist_list[j]['track']['id'])[0]['acousticness'])
            instrumentalness.append(sp.audio_features(tracks_in_playlist_list[j]['track']['id'])[0]['instrumentalness'])
            liveness.append(sp.audio_features(tracks_in_playlist_list[j]['track']['id'])[0]['liveness'])
            valence.append(sp.audio_features(tracks_in_playlist_list[j]['track']['id'])[0]['valence'])
            tempo.append(sp.audio_features(tracks_in_playlist_list[j]['track']['id'])[0]['tempo'])
            uri.append(sp.audio_features(tracks_in_playlist_list[j]['track']['id'])[0]['uri'])
            track_href.append(sp.audio_features(tracks_in_playlist_list[j]['track']['id'])[0]['track_href'])
            analysis_url.append(sp.audio_features(tracks_in_playlist_list[j]['track']['id'])[0]['analysis_url'])
            time_signature.append(sp.audio_features(tracks_in_playlist_list[j]['track']['id'])[0]['time_signature'])

    playlist_tracks_dict = {'id': track_id,
                            'name': name,
                            'popularity': popularity,
                            'type': track_type,
                            'is_local': is_local,
                            'explicit': explicit,
                            'duration_ms': duration_ms,
                            'disc_number': disc_number,
                            'track_number': track_number,
                            'artist_id': artist_id,
                            'artist_name': artist_name,
                            'album_artist_id': album_artist_id,
                            'album_artist_name': album_artist_name,
                            'album_id': album_id,
                            'album_name': album_name,
                            'album_release_date': album_release_date,
                            'album_tracks': album_tracks,
                            'album_type': album_type,
                            'playlist_id': playlist_id,
                            'playlist_name': playlist_name,
                            'playlist_tracks': no_of_tracks_in_playlist,
                            'added_at': added_at,
                            'added_by': added_by,
                            'genres': genres_artist,
                            'album_genres': album_genres,
                            'danceability': danceability,
                            'energy': energy,
                            'key': track_key,
                            'loudness': loudness,
                            'mode': mode,
                            'speechiness': speechiness,
                            'acousticness': acousticness,
                            'instrumentalness': instrumentalness,
                            'liveness': liveness,
                            'valence': valence,
                            'tempo': tempo,
                            'uri': uri,
                            'track_href': track_href,
                            'analysis_url': analysis_url,
                            'time_signature': time_signature
                            }

    playlist_tracks_df = pd.DataFrame(data=playlist_tracks_dict)

    # Create yaml dump
    playlist_dict = dict(zip(playlist_tracks_df['playlist_name'], playlist_tracks_df['playlist_id']))
    with open('spotify_data/playlists.yml', 'w') as outfile:
        yaml.dump(playlist_dict, outfile, default_flow_style=False)

    return playlist_tracks_df
