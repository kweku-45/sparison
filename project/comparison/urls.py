from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/" , views.login , name="login"),
    path("liked/" , views.liked, name="liked"),
    path("sign_out/", views.sign_out, name="sign_out"),
    path("callback/", views.callback, name="callback"),
    path("results/", views.results, name="results"),
    path("add/<name>", views.add , name="add")
]
