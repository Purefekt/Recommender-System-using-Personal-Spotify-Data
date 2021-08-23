import pandas as pd
import string


def get_top_tracks_ids_dataframe(sp):
    """
    We can get the top tracks of the user in 3 different time ranges, short, medium and long.
    We will get the top tracks for all these time ranges and then remove duplicates.

    :param sp: Spotify OAuth
    :return: pandas dataframe of ids of all top tracks
    """

    top_tracks_ids_list = list()

    # short term
    # get more than 50 top tracks since api limits it to 50
    results = sp.current_user_top_tracks(time_range='short_term')
    top_tracks_list = results['items']
    while results['next']:
        results = sp.next(results)
        top_tracks_list.extend(results['items'])
    # get a list of only the track ids
    for i in range(len(top_tracks_list)):
        top_tracks_ids_list.append(top_tracks_list[i]['id'])

    # medium term
    # get more than 50 top tracks since api limits it to 50
    results = sp.current_user_top_tracks(time_range='medium_term')
    top_tracks_list = results['items']
    while results['next']:
        results = sp.next(results)
        top_tracks_list.extend(results['items'])
    # get a list of only the track ids
    for i in range(len(top_tracks_list)):
        top_tracks_ids_list.append(top_tracks_list[i]['id'])

    # long term
    # get more than 50 top tracks since api limits it to 50
    results = sp.current_user_top_tracks(time_range='long_term')
    top_tracks_list = results['items']
    while results['next']:
        results = sp.next(results)
        top_tracks_list.extend(results['items'])
    # get a list of only the track ids
    for i in range(len(top_tracks_list)):
        top_tracks_ids_list.append(top_tracks_list[i]['id'])

    top_tracks_ids_df = pd.DataFrame(top_tracks_ids_list, columns=['id'])
    top_tracks_ids_df = top_tracks_ids_df.drop_duplicates()
    return top_tracks_ids_df


def get_saved_tracks_ids_dataframe(sp):
    """
    We get the ids of all tracks that the user has saved.

    :param sp: Spotify OAuth
    :return: pandas dataframe of saved tracks and corresponding track data
    """
    # get more than 50 top tracks since api limits it to 50
    results = sp.current_user_saved_tracks()
    saved_tracks_list = results['items']
    while results['next']:
        results = sp.next(results)
        saved_tracks_list.extend(results['items'])
    # get a list of only saved track ids
    saved_tracks_ids_list = list()
    for i in range(len(saved_tracks_list)):
        saved_tracks_ids_list.append(saved_tracks_list[i]['track']['id'])

    saved_tracks_ids_df = pd.DataFrame(saved_tracks_ids_list, columns=['id'])
    saved_tracks_ids_df = saved_tracks_ids_df.drop_duplicates()
    return saved_tracks_ids_df


def get_top_tracks_ids_of_top_artists_dataframe(sp):
    """
    We get the ids of 10 top tracks of all top artists of the user.

    :param sp: Spotify OAuth
    :return: pandas dataframe of top 10 tracks ids of all top artists
    """
    # get more than 50 top artists id since api limits it to 50
    results = sp.current_user_top_artists()
    top_artists_list = results['items']
    while results['next']:
        results = sp.next(results)
        top_artists_list.extend(results['items'])

    # get a list of only artists ids
    top_artists_id_list = list()
    for i in range(len(top_artists_list)):
        top_artists_id_list.append(top_artists_list[i]['id'])

    # using these artists id we can get their top 10 tracks
    all_top_artists_top_tracks_ids_list = list()
    for current_artist_id in top_artists_id_list:
        current_artists_top_tracks = sp.artist_top_tracks(current_artist_id)
        for j in range(len(current_artists_top_tracks['tracks'])):
            all_top_artists_top_tracks_ids_list.append(current_artists_top_tracks['tracks'][j]['id'])

    top_tracks_of_top_artists_df = pd.DataFrame(all_top_artists_top_tracks_ids_list, columns=['id'])
    top_tracks_of_top_artists_df = top_tracks_of_top_artists_df.drop_duplicates()
    return top_tracks_of_top_artists_df


def get_random_tracks_ids(sp):
    """
    There is no API call which gives us random songs.
    sp.search() can be used instead with a wildcard mask, %a% means the song will contain an a.
    For all 26 alphabets and 10 numbers we can repeat this 36 times and upto 50 times per wildcard mask or 36*50 tracks.
    I took ~ 1000 random tracks

    :param sp: Spotify OAuth
    :return: pandas dataframe of random tracks ids
    """

    random_tracks_ids_list = list()

    characters = string.ascii_uppercase + string.digits
    for chars in characters:
        search = sp.search(q=f'{chars}%', limit=29)
        for i in range(len(search['tracks']['items'])):
            random_tracks_ids_list.append(search['tracks']['items'][i]['id'])

    random_tracks_ids_df = pd.DataFrame(random_tracks_ids_list, columns=['id'])
    random_tracks_ids_df = random_tracks_ids_df.drop_duplicates()
    return random_tracks_ids_df


def get_tracks_features(sp):
    """
    We will use get_top_tracks_ids_dataframe, get_saved_tracks_ids_dataframe,
    get_top_tracks_ids_of_top_artists_dataframe and get_random_tracks_ids to get the features of those tracks.

    :param sp: Spotify OAuth
    :return: pandas dataframe of features of various tracks
    """

    tracks_ids_list = list()

    # get list of all top tracks ids
    top_tracks_ids_df = get_top_tracks_ids_dataframe(sp=sp)
    tracks_ids_list.extend(top_tracks_ids_df['id'].to_list())

    # get list of all saved tracks ids
    saved_tracks_ids_df = get_saved_tracks_ids_dataframe(sp=sp)
    tracks_ids_list.extend(saved_tracks_ids_df['id'].to_list())

    # get list of all top tracks ids of top artists
    top_tracks_of_top_artists_df = get_top_tracks_ids_of_top_artists_dataframe(sp=sp)
    tracks_ids_list.extend(top_tracks_of_top_artists_df['id'].to_list())

    # get list of all random tracks ids
    random_tracks_ids_df = get_random_tracks_ids(sp=sp)
    tracks_ids_list.extend(random_tracks_ids_df['id'].to_list())

    # 16 cols for track audio features
    popularity, explicit, duration_ms, danceability, energy, key, loudness, mode, speechiness, acousticness, \
    instrumentalness, liveness, valence, tempo, time_signature, genre = list(), list(), list(), list(), list(), \
                                                                        list(), list(), list(), list(), list(), \
                                                                        list(), list(), list(), list(), list(), list(),

    for i in range(len(tracks_ids_list)):

        # Check to skip tracks with broken data
        if sp.audio_features(tracks=tracks_ids_list[i])[0] is None:
            i = i + 1
            print('Skipped a track')

        # Status
        print(f'{round(float(i/len(tracks_ids_list)*100), 2)}% done...')

        current_track_id = tracks_ids_list[i]

        track_data = sp.track(track_id=current_track_id)
        track_audio_features = sp.audio_features(tracks=current_track_id)[0]
        artists_id = track_data['artists'][0]['id']

        popularity.append(track_data['popularity'])
        explicit.append(track_data['explicit'])
        duration_ms.append(track_data['duration_ms'])
        danceability.append(track_audio_features['danceability'])
        energy.append(track_audio_features['energy'])
        key.append(track_audio_features['key'])
        loudness.append(track_audio_features['loudness'])
        mode.append(track_audio_features['mode'])
        speechiness.append(track_audio_features['speechiness'])
        acousticness.append(track_audio_features['acousticness'])
        instrumentalness.append(track_audio_features['instrumentalness'])
        liveness.append(track_audio_features['liveness'])
        valence.append(track_audio_features['valence'])
        tempo.append(track_audio_features['tempo'])
        time_signature.append(track_audio_features['time_signature'])
        genre.append(sp.artist(artist_id=artists_id)['genres'])

    tracks_features = {'id':tracks_ids_list,
                       'popularity': popularity,
                       'explicit': explicit,
                       'duration_ms': duration_ms,
                       'danceability': danceability,
                       'energy': energy,
                       'key': key,
                       'loudness': loudness,
                       'mode': mode,
                       'speechiness': speechiness,
                       'acousticness': acousticness,
                       'instrumentalness': instrumentalness,
                       'liveness': liveness,
                       'valence': valence,
                       'tempo': tempo,
                       'time_signature': time_signature,
                       'genre': genre
                       }

    tracks_features_df = pd.DataFrame(data=tracks_features)
    tracks_features_df = tracks_features_df.drop_duplicates(subset='id')
    return tracks_features_df


def get_recommended_tracks_dataframe(sp):
    """
    We will use the user's top tracks to get recommended tracks.
    For every top track, we can get a maxmimum of 100 recommended tracks.
    We will evaluate our model on this dataset and create playlist from these tracks

    :param sp: Spotify OAuth
    :return: pandas dataframe of recommended tracks based on top tracks and corresponding track features
    """

    # get top tracks ids list using get_top_tracks_ids_dataframe
    top_tracks_ids_df = get_top_tracks_ids_dataframe(sp=sp)
    top_tracks_ids_list = top_tracks_ids_df['id'].to_list()

    # get list of recommended tracks ids (100 each) for each top track
    recommended_tracks_ids_list = list()
    for current_top_track_id in top_tracks_ids_list:
        # get 90 recommended tracks per top track
        recommended_tracks = sp.recommendations(seed_tracks=[current_top_track_id], limit=90)['tracks']
        for i in range(len(recommended_tracks)):
            recommended_tracks_ids_list.append(recommended_tracks[i]['id'])

    # now using this list of recommended tracks ids, we can get their track features

    # 16 cols for track audio features
    popularity, explicit, duration_ms, danceability, energy, key, loudness, mode, speechiness, acousticness, \
    instrumentalness, liveness, valence, tempo, time_signature, genre = list(), list(), list(), list(), list(), \
                                                                        list(), list(), list(), list(), list(), \
                                                                        list(), list(), list(), list(), list(), list(),

    for j in range(len(recommended_tracks_ids_list)):

        # Check to skip tracks with broken data
        if sp.audio_features(tracks=recommended_tracks_ids_list[j])[0] is None:
            j = j + 1
            print('Skipped a track')

        # Status
        print(f'{round(float(j/len(recommended_tracks_ids_list)*100), 2)}% done...')

        current_track_id = recommended_tracks_ids_list[j]

        track_data = sp.track(track_id=current_track_id)
        track_audio_features = sp.audio_features(tracks=current_track_id)[0]
        artists_id = track_data['artists'][0]['id']

        popularity.append(track_data['popularity'])
        explicit.append(track_data['explicit'])
        duration_ms.append(track_data['duration_ms'])
        danceability.append(track_audio_features['danceability'])
        energy.append(track_audio_features['energy'])
        key.append(track_audio_features['key'])
        loudness.append(track_audio_features['loudness'])
        mode.append(track_audio_features['mode'])
        speechiness.append(track_audio_features['speechiness'])
        acousticness.append(track_audio_features['acousticness'])
        instrumentalness.append(track_audio_features['instrumentalness'])
        liveness.append(track_audio_features['liveness'])
        valence.append(track_audio_features['valence'])
        tempo.append(track_audio_features['tempo'])
        time_signature.append(track_audio_features['time_signature'])
        genre.append(sp.artist(artist_id=artists_id)['genres'])

    recommended_tracks_dict = {
        'id':recommended_tracks_ids_list,
        'popularity': popularity,
        'explicit': explicit,
        'duration_ms': duration_ms,
        'danceability': danceability,
        'energy': energy,
        'key': key,
        'loudness': loudness,
        'mode': mode,
        'speechiness': speechiness,
        'acousticness': acousticness,
        'instrumentalness': instrumentalness,
        'liveness': liveness,
        'valence': valence,
        'tempo': tempo,
        'time_signature': time_signature,
        'genre': genre
    }

    recommended_tracks_df = pd.DataFrame(data=recommended_tracks_dict)
    recommended_tracks_df = recommended_tracks_df.drop_duplicates(subset='id')
    return recommended_tracks_df
