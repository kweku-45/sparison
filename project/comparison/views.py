from spotipy import cache_handler, Spotify
from spotipy.cache_handler import CacheFileHandler,CacheHandler
from spotipy import SpotifyException , SpotifyOauthError
from spotipy.oauth2 import SpotifyOAuth
from django.shortcuts import redirect , render
from .authentication import session_cache_path, extract_uuid, oauth, cache_handler
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
from .models import UserProfile , Album, Song, Relationship
from django.contrib.auth.models import User
import uuid as module_uuid
import os
from django.contrib.auth import authenticate, login
from .forms import Form
from .methods import perform_match, follow_back



# Homepage
def home(request):
    return render(request, "home.html"
)

# Assign uuid to individual user
def login(request):
    if not request.session.get("uuid"):
        request.session["uuid"] = extract_uuid
    auth_url = oauth.get_authorize_url()
    return redirect(auth_url)

def callback(request):
    # get authorization code from URL and use code to get access token from Spotify
    try:
        if "code" in request.GET:
            access_token = oauth.get_access_token(request.GET.get("code"))
            request.session["access_token"] = access_token
            sp = Spotify(auth_manager=oauth)
            spotify_user = sp.current_user()
            user__ = User.objects.get_or_create(username=spotify_user['display_name'])[0]
            userprofile = UserProfile.objects.get_or_create(user=user__)[0]
            request.session["username"] = user__.username
            form = Form
        if not oauth.validate_token(cache_handler.get_cached_token()):
            return redirect(reverse("home"))
        return render(
            request, "index.html", {
            "form":form, "username":request.session["username"]
            })
    except SpotifyOauthError:
            return redirect(reverse("login"))



# To get user's Spotify liked songs 
def liked(request):
     #authenticate user by crosschecking UUID code
    if 'uuid' not in request.session:
        return redirect(reverse("login"))
    try:
        sp = Spotify(auth_manager=oauth)
        liked = sp.current_user_saved_tracks(limit=40)['items']
        user = User.objects.get(username = request.session["username"])
        a = []
        for idx, item  in enumerate(liked):
            track = item['track']["name"]
            artist= item["track"]["artists"][0]["name"]
            album_ = item["track"]["album"]["name"]
            tracks = item['track']
            val = tracks['name'] + " - " + tracks['artists'][0]['name']
            a.append(val)
            album = Album.objects.get_or_create(
               Album_name= album_ 
            )[0].save()
          
            song, created = Song.objects.get_or_create(track_name = track,
            artiste_name = artist,
            album = album)
            user.userprofile.liked_songs.add(song)
        return HttpResponse("<br>".join(a))
    except SpotifyException:
        return redirect(reverse("sign_out"))


#handling friendship relations
def add(request, name):
    user = User.objects.get(username = request.session["username"])
    from_person = user.userprofile
    user2 = User.objects.get(username= name)
    to_person= user2.userprofile
    Relationship.objects.get_or_create(
            from_person=from_person,
            to_person= to_person,
            status = 1
            )
    return HttpResponse (f" added {user2.username}")


#Sign Out
def sign_out(request):
        uuid = request.session["uuid"]
        os.remove(f"./.spotify_caches/{uuid}")
        request.session.flush()
        return redirect(reverse("home"))
    #except OSError as e:
        #return HttpResponse("error")
        # print ("Error: %s - %s." % (e.filename, e.strerror))
    
#Implement search for friends.
def results(request):
    if request.method == "GET":
        search_query = request.GET.get("username")
        searched_user = UserProfile.objects.filter(
                user__username__contains=search_query
            )
        
        return render(request,
        "user_search.html", {
            "searched_users":searched_user
        })

#Perform calculation if both users follow each other
def match(request, name):
    user_1= User.objects.get(username = request.session["username"])
    user1= user_1.userprofile
    user_2= User.objects.get(username=name)
    user2= user_2.userprofile
    if follow_back(user1, user2):
        score = perform_match(user1, user2)
        return HttpResponse(score)
    else:
        return HttpResponse("You two don't follow each other")

    


        
    

