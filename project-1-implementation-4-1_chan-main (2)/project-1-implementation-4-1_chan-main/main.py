import requests
from requests_oauthlib import OAuth1
import json
import time
from datetime import date
import datetime
from urllib.parse import urlencode
from pymongo import MongoClient, ASCENDING
import base64

try:
    conn = MongoClient('mongodb://localhost:27017/')
    print("Connected successfully to Twitter Database!!!")
except:  
    print("Could not connect to MongoDB")
db = conn.database
collection = db.Twitter_data
def main_func():  # main function
    count = 0
    while(count < 50):
        url = 'https://api.twitter.com/1.1/search/tweets.json'
        params = {'q': "#spotify", 'lang' : 'en-US'}
        
        r = requests.get(url, auth=auth, params=params)
        count +=1
        status = r.status_code
        if status == 200:
            r = r.json()  # parse the json
            tweets = r['statuses']
            l = len(tweets)
            for tweet in tweets:
                collection.insert_one({'id': l, 'text': tweet['text']})
                l -= 1
main_func()

date.fromisoformat('2022-01-01')

CLIENT_ID = 'yEZsd727g'
SECRET_KEY = 'kraCzSUYyrhBg'

auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

data = {
    'grant_type': 'password',
    'username': 'tkulkar1',
    'password': 'Hendka$361'
}

headers = {'User-Agent': 'Project1'}
res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
TOKEN = res.json()['access_token']
headers = {**headers, **{'Authorization': f'bearer {TOKEN}'}}
headers

link = "https://oauth.reddit.com/r/spotify/"
res = requests.get('https://oauth.reddit.com/r/spotify/', headers=headers)
res.json()

try:
    conn = MongoClient('mongodb://127.0.0.1:27017/')
    print("Connected successfully to Reddit Database!!!")
except:  
    print("Could not connect to MongoDB")
db = conn.database
collection = db.Reddit_data

post_list = res.json()['data']['children']
i = len(post_list)
if len(post_list) > 0:
    for post in post_list:
        collection.insert_one({"id":i,"post":post['data']['title']})
        
client_id = '513ca9651af95af4ee'
client_secret = 'd483296eb4e5cfd'

class SpotifyAPI(object):
    access_token = None
    access_token_expires = datetime.datetime.now()
    access_token_did_expire = True
    client_id = None
    client_secret = None
    token_url = "https://accounts.spotify.com/api/token"
    
    def __init__(self, client_id, client_secret, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = client_id
        self.client_secret = client_secret

    def get_client_credentials(self):
        """
        Returns a base64 encoded string
        """
        client_id = self.client_id
        client_secret = self.client_secret
        if client_secret == None or client_id == None:
            raise Exception("You must set client_id and client_secret")
        client_creds = f"{client_id}:{client_secret}"
        client_creds_b64 = base64.b64encode(client_creds.encode())
        return client_creds_b64.decode()
    
    def get_token_headers(self):
        client_creds_b64 = self.get_client_credentials()
        return {
            "Authorization": f"Basic {client_creds_b64}"
        }
    
    def get_token_data(self):
        return {
            "grant_type": "client_credentials"
        } 
    
    def perform_auth(self):
        token_url = self.token_url
        token_data = self.get_token_data()
        token_headers = self.get_token_headers()
        r = requests.post(token_url, data=token_data, headers=token_headers)
        if r.status_code not in range(200, 299):
            raise Exception("Could not authenticate client.")
            # return False
        data = r.json()
        now = datetime.datetime.now()
        access_token = data['access_token']
        expires_in = data['expires_in'] # seconds
        expires = now + datetime.timedelta(seconds=expires_in)
        self.access_token = access_token
        self.access_token_expires = expires
        self.access_token_did_expire = expires < now
        return True
    
    def get_access_token(self):
        token = self.access_token
        expires = self.access_token_expires
        now = datetime.datetime.now()
        if expires < now:
            self.perform_auth()
            return self.get_access_token()
        elif token == None:
            self.perform_auth()
            return self.get_access_token() 
        return token
    
    def get_resource_header(self):
        access_token = self.get_access_token()
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        return headers
        
        
    def get_resource(self, lookup_id, resource_type='albums', version='v1'):
        endpoint = f"https://api.spotify.com/{version}/{resource_type}/{lookup_id}"
        headers = self.get_resource_header()
        r = requests.get(endpoint, headers=headers)
        if r.status_code not in range(200, 299):
            return {}
        return r.json()
    
    def get_album(self, _id):
        return self.get_resource(_id, resource_type='albums')
    
    def get_artist(self, _id):
        return self.get_resource(_id, resource_type='artists')
    
    def base_search(self, query_params): # type
        headers = self.get_resource_header()
        endpoint = "https://api.spotify.com/v1/search"
        lookup_url = f"{endpoint}?{query_params}"
        r = requests.get(lookup_url, headers=headers)
        if r.status_code not in range(200, 299):  
            return {}
        return r.json()
    
    def search(self, query=None, operator=None, operator_query=None, search_type='artist' ):
        if query == None:
            raise Exception("A query is required")
        if isinstance(query, dict):
            query = " ".join([f"{k}:{v}" for k,v in query.items()])
        if operator != None and operator_query != None:
            if operator.lower() == "or" or operator.lower() == "not":
                operator = operator.upper()
                if isinstance(operator_query, str):
                    query = f"{query} {operator} {operator_query}"
        query_params = urlencode({"q": query, "type": search_type.lower()})
        #print(query_params)
        return self.base_search(query_params)

spotify = SpotifyAPI(client_id, client_secret)

tracks = spotify.search({"track":"Time"}, search_type="track")

try:
    conn = MongoClient('mongodb://127.0.0.1:27017/')
    print("Connected successfully to Spotify Database!!!")
except:  
    print("Could not connect to MongoDB")
db = conn.database
collection = db.Spotify_data

tracks_list = tracks['tracks']['items']
if len(tracks_list) > 0:
    for track in tracks_list:
        db.Spotify_data.create_index("album",unique=True)
        break
        collection.insert_one({'id':track['artists'][0]['id'],'album':track['name'],'artist':track['artists'][0]['name']})
        

