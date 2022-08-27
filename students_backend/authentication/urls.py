"""
List of all the auth routes...
"""
from django.contrib import admin
from django.urls import path
from authentication import signup

urlpatterns = [
    path("signUp/", signup.signUp),
]
