import pandas as pd
import yaml


def get_top_artists_dataframe(sp):
    """
    :param sp: Spotify OAuth
    :return: pandas dataframe of top artists and corresponding artists data
    """
    # get more than 50 top artists since api limits it to 50
    results = sp.current_user_top_artists()
    top_artists_list = results['items']
    while results['next']:
        results = sp.next(results)
        top_artists_list.extend(results['items'])

    artist_id, uri, artist_type, name, genres, followers = list(), list(), list(), list(), list(), list()

    for i in range(len(top_artists_list)):
        # Status
        print(f'{round(float((i / len(top_artists_list)) * 100),2)}% done...')

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
    top_artists_df.drop_duplicates(subset='id')
    return top_artists_df


def get_followed_artists_dataframe(sp):
    """
    :param sp: Spotify OAuth
    :return: pandas dataframe of followed artists and corresponding artists data
    """
    # get more than 50 followed artists since api limits it to 50
    results = sp.current_user_followed_artists()
    followed_artists_list = results['artists']['items']
    while results['artists']['next']:
        results = sp.next(results['artists'])
        followed_artists_list.extend(results['artists']['items'])

    artist_id, uri, artist_type, name, genres, followers = list(), list(), list(), list(), list(), list(),

    for i in range(len(followed_artists_list)):
        # Status
        print(f'{round(float((i / len(followed_artists_list)) * 100), 2)}% done...')

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
    followed_artists_df.drop_duplicates(subset='id')
    return followed_artists_df


def get_top_tracks_dataframe(sp):
    """
    :param sp: Spotify OAuth
    :return: pandas dataframe of top tracks and corresponding track data
    """
    # get more than 50 top tracks since api limits it to 50
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
        print(f'{round(float((i / len(top_tracks_list)) * 100), 2)}% done...')

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
        genres_artist.append(sp.artists({artist_id[-1]})['artists'][0]['genres'])
        album_genres.append(sp.artists({album_artist_id[-1]})['artists'][0]['genres'])

        current_track_id = track_id[-1]
        current_track_audio_features = sp.audio_features(current_track_id)

        danceability.append(current_track_audio_features[0]['danceability'])
        energy.append(current_track_audio_features[0]['energy'])
        track_key.append(current_track_audio_features[0]['key'])
        loudness.append(current_track_audio_features[0]['loudness'])
        mode.append(current_track_audio_features[0]['mode'])
        speechiness.append(current_track_audio_features[0]['speechiness'])
        acousticness.append(current_track_audio_features[0]['acousticness'])
        instrumentalness.append(current_track_audio_features[0]['instrumentalness'])
        liveness.append(current_track_audio_features[0]['liveness'])
        valence.append(current_track_audio_features[0]['valence'])
        tempo.append(current_track_audio_features[0]['tempo'])
        uri.append(current_track_audio_features[0]['uri'])
        track_href.append(current_track_audio_features[0]['track_href'])
        analysis_url.append(current_track_audio_features[0]['analysis_url'])
        time_signature.append(current_track_audio_features[0]['time_signature'])

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
    top_tracks_df.drop_duplicates(subset='id')
    return top_tracks_df


def get_saved_tracks_dataframe(sp):
    """
    :param sp: Spotify OAuth
    :return: pandas dataframe of saved tracks and corresponding track data
    """
    # get more than 50 top tracks since api limits it to 50
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
        print(f'{round(float((i / len(saved_tracks_list)) * 100), 2)}% done...')

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
        current_artist_id = artist_id[-1]
        current_album_artist_id = album_artist_id[-1]
        current_track_id = track_id[-1]
        current_track_audio_features = sp.audio_features(current_track_id)

        genres_artist.append(sp.artists({current_artist_id})['artists'][0]['genres'])
        album_genres.append(sp.artists({current_album_artist_id})['artists'][0]['genres'])

        danceability.append(current_track_audio_features[0]['danceability'])
        energy.append(current_track_audio_features[0]['energy'])
        track_key.append(current_track_audio_features[0]['key'])
        loudness.append(current_track_audio_features[0]['loudness'])
        mode.append(current_track_audio_features[0]['mode'])
        speechiness.append(current_track_audio_features[0]['speechiness'])
        acousticness.append(current_track_audio_features[0]['acousticness'])
        instrumentalness.append(current_track_audio_features[0]['instrumentalness'])
        liveness.append(current_track_audio_features[0]['liveness'])
        valence.append(current_track_audio_features[0]['valence'])
        tempo.append(current_track_audio_features[0]['tempo'])
        uri.append(current_track_audio_features[0]['uri'])
        track_href.append(current_track_audio_features[0]['track_href'])
        analysis_url.append(current_track_audio_features[0]['analysis_url'])
        time_signature.append(current_track_audio_features[0]['time_signature'])

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
    saved_tracks_df.drop_duplicates(subset='id')
    return saved_tracks_df


def get_playlist_tracks_dataframe(sp):
    """
    :param sp: Spotify OAuth
    :return: pandas dataframe of tracks in playlists and corresponding track data
    """
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
            print('Skipped a playlist')
            i = i + 1

        # Data used for 3 playlist columns
        current_playlist_id = playlists[i]['id']
        current_playlist_name = playlists[i]['name']
        no_of_tracks_in_current_playlist = sp.playlist_tracks(current_playlist_id)['total']

        # get more than 50 top tracks since api limits it to 50
        results = sp.playlist_tracks(current_playlist_id)
        tracks_in_playlist_list = results['items']
        while results['next']:
            results = sp.next(results)
            tracks_in_playlist_list.extend(results['items'])

        # Status
        print(f'{round(float((i / len(playlists)) * 100), 2)}% done...')

        # Loop through all tracks in the current playlist
        for j in range(no_of_tracks_in_current_playlist):

            # Checks to skip tracks with broken data
            if tracks_in_playlist_list[j]['track']['album']['artists'] == []:
                print('Skipped a track')
                j = j + 1
            if tracks_in_playlist_list[j]['track']['album']['artists'] == []:
                print('Skipped a track')
                j = j + 1
            if sp.audio_features(tracks_in_playlist_list[j]['track']['id'])[0] is None:
                j = j + 1
                print('Skipped a track')

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
            current_track_id = sp.audio_features(tracks_in_playlist_list[j]['track']['id'])

            genres_artist.append(sp.artist(tracks_in_playlist_list[j]['track']['artists'][0]['id'])['genres'])
            album_genres.append(
                sp.artist(tracks_in_playlist_list[j]['track']['album']['artists'][0]['id'])['genres'])
            danceability.append(current_track_id[0]['danceability'])
            energy.append(current_track_id[0]['energy'])
            track_key.append(current_track_id[0]['key'])
            loudness.append(current_track_id[0]['loudness'])
            mode.append(current_track_id[0]['mode'])
            speechiness.append(current_track_id[0]['speechiness'])
            acousticness.append(current_track_id[0]['acousticness'])
            instrumentalness.append(current_track_id[0]['instrumentalness'])
            liveness.append(current_track_id[0]['liveness'])
            valence.append(current_track_id[0]['valence'])
            tempo.append(current_track_id[0]['tempo'])
            uri.append(current_track_id[0]['uri'])
            track_href.append(current_track_id[0]['track_href'])
            analysis_url.append(current_track_id[0]['analysis_url'])
            time_signature.append(current_track_id[0]['time_signature'])

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
    playlist_tracks_df.drop_duplicates(subset='id')

    # Create yaml dump
    playlist_dict = dict(zip(playlist_tracks_df['playlist_name'], playlist_tracks_df['playlist_id']))
    with open('spotify_data/playlists.yml', 'w') as outfile:
        yaml.dump(playlist_dict, outfile, default_flow_style=False)

    return playlist_tracks_df


def get_recommendation_track_dataframe(sp):
    """
    :param sp: Spotify OAuth
    :return: pandas dataframe of recommended tracks based on top tracks and corresponding track data
    """
    # We will use the user's top tracks to get recommendation
    # Per top track, we can get a maximum of 100 recommended tracks
    # If we have 60 top tracks then we can get 6000 recommended tracks

    # get more than 50 top tracks since api limits it to 50
    results = sp.current_user_top_tracks()
    top_tracks_list = results['items']
    while results['next']:
        results = sp.next(results)
        top_tracks_list.extend(results['items'])

    # Get list of only top track id
    top_track_ids_list = list()
    for i in range(len(top_tracks_list)):
        top_track_ids_list.append(top_tracks_list[i]['id'])

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

    for j in range(len(top_track_ids_list)):

        # Status
        print(f'{round(float((j / len(top_track_ids_list)) * 100), 2)}% done...')

        current_top_track_id = top_track_ids_list[j]

        # get 100 recommended tracks for current top track
        recommended_tracks = sp.recommendations(seed_tracks=[current_top_track_id], limit=100)

        # loop through all 100 recommended tracks and get the data of those tracks
        for k in range(len(recommended_tracks['tracks'])):

            # Checks to skip tracks with broken data
            if sp.audio_features(recommended_tracks['tracks'][k]['id'])[0] is None:
                k = k + 1
                print('Skipped a track')

            # Tracks
            track_id.append(recommended_tracks['tracks'][k]['id'])
            name.append(recommended_tracks['tracks'][k]['name'])
            popularity.append(recommended_tracks['tracks'][k]['popularity'])
            track_type.append(recommended_tracks['tracks'][k]['type'])
            is_local.append(recommended_tracks['tracks'][k]['is_local'])
            explicit.append(recommended_tracks['tracks'][k]['explicit'])
            duration_ms.append(recommended_tracks['tracks'][k]['duration_ms'])
            disc_number.append(recommended_tracks['tracks'][k]['disc_number'])
            track_number.append(recommended_tracks['tracks'][k]['track_number'])
            artist_id.append(recommended_tracks['tracks'][k]['artists'][0]['id'])
            artist_name.append(recommended_tracks['tracks'][k]['artists'][0]['name'])
            album_artist_id.append(recommended_tracks['tracks'][k]['album']['artists'][0]['id'])
            album_artist_name.append(recommended_tracks['tracks'][k]['album']['artists'][0]['name'])
            album_id.append(recommended_tracks['tracks'][k]['album']['id'])
            album_name.append(recommended_tracks['tracks'][k]['album']['name'])
            album_release_date.append(recommended_tracks['tracks'][k]['album']['release_date'])
            album_tracks.append(recommended_tracks['tracks'][k]['album']['total_tracks'])
            album_type.append(recommended_tracks['tracks'][k]['album']['type'])

            # Track audio features
            genres_artist.append(sp.artists({artist_id[-1]})['artists'][0]['genres'])
            album_genres.append(sp.artists({album_artist_id[-1]})['artists'][0]['genres'])

            current_track_id = track_id[-1]
            current_track_audio_features = sp.audio_features(current_track_id)

            danceability.append(current_track_audio_features[0]['danceability'])
            energy.append(current_track_audio_features[0]['energy'])
            track_key.append(current_track_audio_features[0]['key'])
            loudness.append(current_track_audio_features[0]['loudness'])
            mode.append(current_track_audio_features[0]['mode'])
            speechiness.append(current_track_audio_features[0]['speechiness'])
            acousticness.append(current_track_audio_features[0]['acousticness'])
            instrumentalness.append(current_track_audio_features[0]['instrumentalness'])
            liveness.append(current_track_audio_features[0]['liveness'])
            valence.append(current_track_audio_features[0]['valence'])
            tempo.append(current_track_audio_features[0]['tempo'])
            uri.append(current_track_audio_features[0]['uri'])
            track_href.append(current_track_audio_features[0]['track_href'])
            analysis_url.append(current_track_audio_features[0]['analysis_url'])
            time_signature.append(current_track_audio_features[0]['time_signature'])

    recommended_tracks_dict = {'id': track_id,
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

    recommended_tracks_df = pd.DataFrame(data=recommended_tracks_dict)
    recommended_tracks_df.drop_duplicates(subset='id')
    return recommended_tracks_df
