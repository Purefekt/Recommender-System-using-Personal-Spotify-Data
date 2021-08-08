import pandas as pd


def get_top_artists_dataframe(sp):
    results = sp.current_user_top_artists()
    top_artists_list = results['items']
    while results['next']:
        results = sp.next(results)
        top_artists_list.extend(results['items'])

    artist_id = list()
    uri = list()
    artist_type = list()
    name = list()
    genres = list()
    followers = list()

    for i in range(len(top_artists_list)):
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

    artist_id = list()
    uri = list()
    artist_type = list()
    name = list()
    genres = list()
    followers = list()

    for i in range(len(followed_artists_list)):
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

    track_id = list()
    name = list()
    popularity = list()
    track_type = list()
    is_local = list()
    explicit = list()
    duration_ms = list()
    disc_number = list()
    track_number = list()
    artist_id = list()
    artist_name = list()
    album_artist_id = list()
    album_artist_name = list()
    album_id = list()
    album_name = list()
    album_release_date = list()
    album_tracks = list()
    album_type = list()
    genres_artist = list()
    album_genres = list()
    danceability = list()
    energy = list()
    track_key = list()
    loudness = list()
    mode = list()
    speechiness = list()
    acousticness = list()
    instrumentalness = list()
    liveness = list()
    valence = list()
    tempo = list()
    uri = list()
    track_href = list()
    analysis_url = list()
    time_signature = list()

    for i in range(len(top_tracks_list)):
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

    track_id = list()
    name = list()
    popularity = list()
    track_type = list()
    is_local = list()
    explicit = list()
    duration_ms = list()
    disc_number = list()
    track_number = list()
    artist_id = list()
    artist_name = list()
    album_artist_id = list()
    album_artist_name = list()
    album_id = list()
    album_name = list()
    album_release_date = list()
    album_tracks = list()
    album_type = list()
    added_at = list()
    genres_artist = list()
    album_genres = list()
    danceability = list()
    energy = list()
    track_key = list()
    loudness = list()
    mode = list()
    speechiness = list()
    acousticness = list()
    instrumentalness = list()
    liveness = list()
    valence = list()
    tempo = list()
    uri = list()
    track_href = list()
    analysis_url = list()
    time_signature = list()

    for i in range(len(saved_tracks_list)):
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
