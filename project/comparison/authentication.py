<<<<<<< HEAD
from spotipy.oauth2 import SpotifyOAuth
from django.conf import settings

oauth = SpotifyOAuth(
    redirect_uri="http://127.0.0.1:8000/spotify/authorize",
    scope='user-library-read'
)


# oauth2 =  SpotifyOAuth(
#     redirect_uri="http://127.0.0.1:8000/spotify/authorize",
    
# )

authorize_url = oauth.get_authorize_url()
 
=======
from django.conf import settings
import os
from spotipy.oauth2 import SpotifyOAuth
import uuid


uuid_ = uuid.uuid4() 
uuid = str(uuid_)
caches_folder = "./.spotify_caches/"
if not os.path.exists(caches_folder):
    os.makedirs(caches_folder)

def session_cache_path(uuid):
    return caches_folder + uuid


oauth = SpotifyOAuth(
  redirect_uri="http://127.0.0.1:8000/spotify/callback",
    scope='user-library-read',
    show_dialog=True,
    cache_path=session_cache_path(uuid)
)








>>>>>>> b54d9c04 (slight changes)
