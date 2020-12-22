from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    #path("", views.home, name="home"),
    path("login/" , views.login , name="login"),
    path("authorize/", views.callback, name="redirect"),
    path("liked/" , views.liked, name="liked"),
    # path("liked2/", views.liked2, name="liked2")
=======
    path("home/", views.home, name="home"),
    path("" , views.login , name="login"),
    path("liked/" , views.liked, name="liked"),
    path("sign_out/", views.sign_out, name="sign_out"),
    path("current/", views.current_user, name="current"),
    path("callback/", views.callback, name="callback")
>>>>>>> b54d9c04 (slight changes)
]
