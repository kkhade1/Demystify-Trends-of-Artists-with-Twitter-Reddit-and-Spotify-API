from os import times
from numpy import expand_dims
import pymongo 
import pandas as pd
from pymongo import MongoClient
from urllib.parse import urlparse
import urllib.parse
import requests
import time as tim
import pandas as pd
from urllib.parse import urlparse
import pandas as pd
from tabulate import tabulate
from slugify import slugify
import json

def getredditAnalysis():
        

    CLIENT_ID = '7cf4b873cdf5c'
    CLIENT_SECRET = 'bb3469c4efe2'

    AUTH_URL = 'https://accounts.spotify.com/api/token'

    auth_response = requests.post(AUTH_URL, {'grant_type': 'client_credentials','client_id': CLIENT_ID,'client_secret': CLIENT_SECRET,})

    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']

    headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}

    BASE_URL = 'https://api.spotify.com/v1/'

    conn = MongoClient('mongodb://localhost:27017')

    db = conn.database
    collection = db.Reddit_data

    artist_id = []
    for urls in collection.find({},{ "_id": 0, "id": 0}):
        links = (urls['url'])
        parts = urlparse(links)
        directories = parts.path.strip('/').split('/')
        artist_id.append(directories[1])

    count_Playlists = 13
    count_Tracks = 6
    count_Artists = 0
    Final_artist_list = []
    for i in artist_id:
        r = requests.get(BASE_URL + 'playlists/' + i, headers=headers)
        list = r.json()['tracks']['items']
        for post in list:
            singer = (post['track']['album']['artists'])
            for post in singer:
                Final_artist_list.append(post['name'])

    Final_artist_list = pd.DataFrame(Final_artist_list)

    return(count_Playlists, count_Tracks, count_Artists)
