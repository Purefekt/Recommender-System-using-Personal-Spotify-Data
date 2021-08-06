# Recommender System using Personal Spotify Data

## Getting the Music Data
To start we need to acquire our Spotify music data.
### Accessing Spotify API
We will get the Spotify data using the Spotify Web API. For that we need a Spotify developer account.
1. Go to [Spotify for Developers](https://developer.spotify.com/).
2. Go to Dashboard and Login.
3. Select 'My Side Project', add an App name and App description.
4. Make a note of the Client ID and Client Secret.
5. Go to 'EDIT SETTINGS' and set up 'Redirect URIs' to 'http://localhost:9001/callback' and save.

### Creating Details JSON File
Now we create the details json file where we store the Client ID, Client Secret and Redirect URI. The format is given in the ```spotify_details_template.json``` file and looks like this:
```buildoutcfg
{
    "client_id": " ",
    "client_secret": " ",
    "redirect_uri": " "
}
```
### Connecting to the Spotify API
We will use the [spotipy](https://spotipy.readthedocs.io/en/2.18.0/) python library to interact with the Spotify Web API.  
The python file ```connect_to_api.py``` establishes the connection with the Spotify API. It has a function called ```connect_to_api(spotify_json_file)```, it takes in the details json file and uses the given information to connect to Spotify Web API. It returns a spotify api client object which can be used for further function calls.

### Pulling Various Types of Spotify Data
1. Top Artists - We use the function ```current_user_top_artists()``` which returns different information about the user's top artists. We only care about a few of these like name, genre, id, etc. so we create a pandas dataframe of the relevant information.