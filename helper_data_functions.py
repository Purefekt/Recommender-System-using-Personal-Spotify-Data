import pandas as pd


def get_top_artists_dataframe(top_artists):
    """
    :param top_artists: top artists Spotify Data
    :return: pandas dataframe of id, uri, type, name, genre and followers of top artists
    """
    artist_id = list()
    uri = list()
    artist_type = list()
    name = list()
    genres = list()
    followers = list()

    for i in range(len(top_artists['items'])):
        artist_id.append(top_artists['items'][i]['id'])
        uri.append(top_artists['items'][i]['uri'])
        artist_type.append(top_artists['items'][i]['type'])
        name.append(top_artists['items'][i]['name'])
        genres.append(top_artists['items'][i]['genres'])
        followers.append(top_artists['items'][i]['followers']['total'])

    top_artists_dict = {'id': artist_id,
                        'uri': uri,
                        'type': artist_type,
                        'name': name,
                        'genres': genres,
                        'followers': followers
                        }

    top_artists_df = pd.DataFrame(data=top_artists_dict)
    return top_artists_df
