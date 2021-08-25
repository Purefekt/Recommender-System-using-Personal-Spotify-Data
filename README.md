# Recommender System using Personal Spotify Data
Creating playlists using various Machine Learning classification algorithms on friend's Spotify data curated using the Spotify Web API.

## Getting the Music Data
To start we need to acquire the Spotify music data. This requires connecting to the Spotify Web API and pulling different data that we might need.
### Getting API credentials
1. Go to [Spotify for Developers](https://developer.spotify.com/).
2. Go to Dashboard and Login.
3. Select 'My Side Project', add an App name and App description.
4. Make a note of the Client ID and Client Secret.
5. Go to 'EDIT SETTINGS' and set up 'Redirect URIs' to 'http://localhost:9001/callback' and save.  
**Note**: Sometimes the API stops responding when too much data is called. When this happens delete this 'My Side Project' and make a brand new one. Use the same 'Redirect URI' and make a note of the new Client ID and Client Secret. Also **DELETE** the .cache hidden file everytime when this step is repeated.

### Creating Credentials JSON File
Now we create the credentials json file where we store the Client ID, Client Secret and Redirect URI. The format is given in the ```spotify_credentials_template.json``` file and looks like this:
```
{
    "client_id": " ",
    "client_secret": " ",
    "redirect_uri": "http://localhost:9001/callback"
}
```
### Connecting to the Spotify API
We will use the [spotipy](https://spotipy.readthedocs.io/en/2.18.0/) python library to interact with the Spotify Web API.  
The python file ```connect_to_api.py``` establishes the connection with the Spotify API. It has a function called ```connect_to_api(spotify_credentials_json)```, it takes in the credentials json file and uses the given information to connect to Spotify Web API. It returns a spotify api client object which can be used for further function calls like getting the user's name, user's top tracks, etc.

### Pulling Various Types of Spotify Data
I have defined various functions in ```helper_data_functions.py``` which can be called to get dataframes of the required data.  
```music_data.py``` calls these functions and serializes the data.  

We get the follow data:
1. Track ids of user's top tracks
2. Track ids of user's saved tracks
3. Track ids of top 10 tracks of user's top artists
4. Track ids of random tracks (these will be labelled 0)
5. Track features comprising of all tracks in 1-4
6. Track features of recommended tracks (~7500 tracks recommended via 1-3)
