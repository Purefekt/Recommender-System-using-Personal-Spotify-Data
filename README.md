# Recommender System using Personal Spotify Data

## Summary
8 Machine Learning supervised classification algorithms were used on my personal spotify data collected using Spotify Web API. These algorithms were used to create a recommender playlist. The features were scaled and normalized when needed and the hyperparameters were tuned to get the best results. The final playlist was sent back to my spotify account using the api.  

## Getting the data with Spotify Web API
 The data was collcted using Spotify Web API, more details [here](https://github.com/Purefekt/Recommender-System-using-Personal-Spotify-Data#getting-the-music-data). This was a binary classification problem, my top tracks, saved tracks and my top artists' top 10 tracks (for each artist) became the 1 class. Then some random tracks were pulled (almost as much as the number of tracks in 1 class) and were labelled as 0. Spotify has assigned track features like loudness, acousticness, tempo, genres etc to each track. These became the features of the dataset. Spotify also provides recommended tracks, i pulled around ~7000 of these, these became the tracks to be evaluated on. Any track in this set with a high enough probability would make it to the recommender playlist.

## Cleaning the Data
Duplicate tracks were removed and the labelled data was divided into training and test datasets. The 7000 or so recommended tracks became the evaluation dataset and the druplicate tracks were removed. Details are in this jupyter notebook -> [get_training_testing_and_evaluation_data.ipynb](get_training_testing_and_evaluation_data.ipynb)

## Algorithms used
1. Logistic Regression -> [logistic_regression.ipynb](logistic_regression.ipynb)
2. Naive Bayes -> [naive_bayes.ipynb](naive_bayes.ipynb)
3. Stochastic Gradient Descent -> [stochastic_gradient_descent.ipynb](stochastic_gradient_descent.ipynb)
4. K-Nearest Neighbours -> [k-nearest_neighbours.ipynb](k-nearest_neighbours.ipynb)
5. Decision Tree -> [decision_tree.ipynb](decision_tree.ipynb)
6. Random Forest -> [random_forest.ipynb](random_forest.ipynb)
7. Support Vector Machine -> [support_vector_machine.ipynb](support_vector_machine.ipynb)
8. XGBoost -> [xgboost.ipynb](xgboost.ipynb)

## Results
All the algorithms were compared using the F1 score metric. K-Nearest Neighbours and Random Forest were the best algorithms. Both of these were then used (alone with feature scaling for KNN and best hyperparameters) on the evaluation dataset and tracks were classified into 1 and 0. From the tracks labelled as 1, the tracks with higher probability (>=1 for KNN and >=0.9 Random Forest) were then selected to be in the recommender playlist. Details are found in this jupyter notebook --> [final_results.ipynb](final_results.ipynb)

## Sending Playlists back to Spotify using the Web API
2 Playlists were created, K-Nearest Neighbours(1737 tracks) and Random Forest(300 tracks). Both of these playlists were sent to my spotify account using the Spotify web API using this python script -->  [send_recommended_playlists_to_spotify.py](send_recommended_playlists_to_spotify.py)

## Final Thoughts
This was a fun project where i learned how to work with APIs, collect data, clean data, split data into train and testing datasets. I learned various supervised classification machine learning algorithms and when to apply feature scaling and what hyperparameters to tune. The final playlist is great and i have lots of new songs to listen to.

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
