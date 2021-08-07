import pandas as pd


def get_top_artists_unlimited(sp, sp_call):
    """
    Since we can get a maximum of 50 top artists with the provided API request, we use the following function to get
    more than 50 results
    :param sp: API client variable
    :param sp_call: API request
    :return: list of all top artists of the user
    """
    results = sp_call
    items = results['items']
    while results['next']:
        results = sp.next(results)
        items.extend(results['items'])

    return items


def get_top_artists_dataframe(top_artists_list):
    """
    :param top_artists_list: list of user's top artists
    :return: dataframe of user's top artists
    """
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


def get_followed_artists_unlimited(sp, sp_call):
    """
    Since we can get a maximum of 50 followed artists with the provided API request, we use the following function to
    get more than 50 results
    :param sp: API client variable
    :param sp_call: API request
    :return: list of all followed artists by the user
    """
    results = sp_call
    items = results['artists']['items']
    while results['artists']['next']:
        results = sp.next(results['artists'])
        items.extend(results['artists']['items'])

    return items


def get_followed_artists_dataframe(followed_artists_list):
    """
    :param followed_artists_list: list of user's followed artists
    :return: dataframe of user's followed artists
    """
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


def get_top_tracks_unlimited(sp, sp_call):
    """
    Since we can get a maximum of 50 top tracks with the provided API request, we use the following function to
    get more than 50 results
    :param sp: API client variable
    :param sp_call: API request
    :return: list of top tracks of the user
    """
    results = sp_call
    items = results['items']
    while results['next']:
        results = sp.next(results)
        items.extend(results['items'])

    return items


def get_top_tracks_df(top_tracks_list):
    """
    :param top_tracks_list: list of user's top tracks
    :return: dataframe of user's top tracks
    """
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
                       'album_type': album_type
                       }

    top_tracks_df = pd.DataFrame(data=top_tracks_dict)
    return top_tracks_df
