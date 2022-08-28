"""
List of all the auth routes...
"""
from django.contrib import admin
from django.urls import path
from authentication import signup
from authentication import login


urlpatterns = [
    path("signUp/", signup.signUp),
    path("login/", login.login),
    path("reset/", login.reset)
]
