<<<<<<< HEAD

=======
>>>>>>> b54d9c04 (slight changes)
from spotipy import Spotify
from spotipy import SpotifyException
from spotipy.oauth2 import SpotifyOAuth
from django.shortcuts import redirect , render
from .authentication import oauth, uuid, session_cache_path
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
import json
from .models import UserProfile , Album, Song
from django.contrib.auth.models import User
import uuid as module_uuid
import os
from django.contrib.auth import authenticate, login

#Assign uuid to individual user
def login(request):
    if not request.session.get("uuid"):
       request.session["uuid"] = uuid
    auth_url = oauth.get_authorize_url()
    return redirect(auth_url)
    

def callback(request):
    if "code" in request.GET:
        # Step 3. Being redirected from Spotify auth page
        oauth.get_access_token(request.GET.get("code"))
        return render(
        request, "try.html"
        )
        

    if not oauth.get_cached_token():
    # Step 2. Display sign in link when no token
        auth_url = oauth.get_authorize_url()
        return redirect(reverse("login"))

   
def liked(request):

    try:
        sp = Spotify(auth_manager=oauth)
        liked = sp.current_user_saved_tracks(limit=30)['items']
        spotify_user = sp.current_user()
        user__ , created = User.objects.get_or_create(username=spotify_user['uri'], first_name=spotify_user["display_name"])
        userprofile = UserProfile.objects.get_or_create(user=user__)[0]
            

        a = []

        for idx, item in enumerate(liked):
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

            songs_available = userprofile.liked_songs.all()

            if song in songs_available:
                continue

            else:
                user__.userprofile.liked_songs.add(song)
        
        return HttpResponse("<br>".join(a))

    except SpotifyException:
        return redirect(reverse("sign_out"))

def sign_out(request):
    try:
        # Remove the CACHE file (.cache-test) so that a new user can authorize.
        os.remove(session_cache_path(uuid))
        request.session.flush()
    except OSError as e:
        print ("Error: %s - %s." % (e.filename, e.strerror))

    return redirect(reverse("home"))

def current_user(request):
    if not oauth.get_cached_token():
        return redirect(reverse("login"))
    sp = Spotify(auth_manager=oauth)
    current_user= sp.current_user()
    return HttpResponse(f"Welcome,{current_user['display_name']}")


def home(request): 
    return render(request, 
        template_name= "display.html"
    )


<<<<<<< HEAD
def match(request):
    user1=UserProfile.objects.get(id=2)
    user2=UserProfile.objects.get(id=1)
    q1= user1.liked_songs.all()
    q2=user2.liked_songs.all()
    q4 = q1&q2
    match= q4.count()

    return HttpResponse(str(match))
=======



>>>>>>> b54d9c04 (slight changes)
    

