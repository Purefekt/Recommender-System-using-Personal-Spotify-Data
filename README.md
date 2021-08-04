# Recommender System using Personal Spotify Data

## Accessing Spotify API
We will get the Spotify data using the Spotify API. For that we need a Spotify developer account.
1. Go to [Spotify for Developers](https://developer.spotify.com/).
2. Go to Dashboard and Login.
3. Select 'My Side Project', add an App name and App description.
4. Get the Client ID, Client Secret .
5. Go to 'EDIT SETTINGS' and set up 'Redirect URIs' to 'http://localhost:9001/callback' and save.

## Getting the Music Data
We will use **spotipy** python package to pull the music data from the Spotify API. 