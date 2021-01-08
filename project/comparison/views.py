from spotipy import Spotify
from spotipy import SpotifyException , SpotifyOauthError
from spotipy.oauth2 import SpotifyOAuth
from django.shortcuts import redirect , render
from .authentication import oauth, uuid, session_cache_path
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
import json
from .models import UserProfile , Album, Song, Relationship
from django.contrib.auth.models import User
import uuid as module_uuid
import os
from django.contrib.auth import authenticate, login
from .forms import Form
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string

#Home Page
def home(request):
    return render(
### Yet to do this
    )


# Assign uuid to individual user
def login(request):
    if not request.session.get("uuid"):
       request.session["uuid"] = uuid
    auth_url = oauth.get_authorize_url()
    return redirect(auth_url)
    

def callback(request):
    if "code" in request.GET:
        # Step 3. Being redirected from Spotify auth page
        access_token = oauth.get_access_token(request.GET.get("code"))
        request.session["access_token"] = access_token
        sp = Spotify(auth_manager=oauth)
        spotify_user = sp.current_user()
        user__ = User.objects.get_or_create(username=spotify_user['display_name'])[0]
        userprofile = UserProfile.objects.get_or_create(user=user__)[0]
        request.session["username"] = user__.username
        form = Form
        return render(
        request, "index.html", {
            "form":form
        })

    else:
        return redirect(reverse("login"))
    

    if not oauth.get_cached_token():
    # Step 2. Display sign in link when no token
        auth_url = oauth.get_authorize_url()
        return redirect(reverse("login"))



# To get user's Spotify liked songs 
def liked(request):

    # authenticate user
    if 'uuid' not in request.session:
        print("uuid not in session, redirecting to login")
        return redirect(reverse("login"))
    try:
        sp = Spotify(auth_manager=oauth)
        liked = sp.current_user_saved_tracks(limit=30)['items']
        user = User.objects.get(username = request.session["username"])
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

            user.userprofile.liked_songs.add(song)
        
        return HttpResponse("<br>".join(a))

    except SpotifyException:
        return redirect(reverse("sign_out"))



#Create view to handle friendships

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
    
    from_user_liked_songs = from_person.liked_songs.all()
    to_user_liked_songs = to_person.liked_songs.all()
    count = from_user_liked_songs&to_user_liked_songs
    display_count = count.count()
    return HttpResponse(display_count)





# Unfinished logic
def sign_out(request):
    try:
        os.remove(session_cache_path(uuid))
        request.session.flush()
    except OSError as e:
        print ("Error: %s - %s." % (e.filename, e.strerror))

    return redirect(reverse("home"))


# Implement search for friends.
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
        
    

