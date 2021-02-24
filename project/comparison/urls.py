from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/" , views.login , name="login"),
    path("liked/" , views.liked, name="liked"),
    path("logout/", views.sign_out, name="logout"),
    path("callback/", views.callback, name="callback"),
    path("results/", views.results, name="results"),
    path("add/<name>", views.add , name="add"),
    path("match/<name>", views.match, name="match"),]

