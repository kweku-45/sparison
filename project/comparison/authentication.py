from django.conf import settings
import os
from spotipy.oauth2 import SpotifyOAuth
import uuid
from spotipy import CacheFileHandler
from spotipy import Spotify

caches_folder = "./.spotify_caches/"
if not os.path.exists(caches_folder):
    os.makedirs(caches_folder)

#Create session path with UUID
def session_cache_path(): 
    return caches_folder + str(uuid.uuid4())

cache_path = session_cache_path()

#Extract UUID from path
def extract_uuid(cache_path):
    return cache_path[18:]


cache_handler = CacheFileHandler(cache_path = cache_path)
oauth = SpotifyOAuth(
        redirect_uri="http://127.0.0.1:8000/spotify/callback",
        scope='user-library-read',
        show_dialog=True,
        cache_handler = cache_handler)













