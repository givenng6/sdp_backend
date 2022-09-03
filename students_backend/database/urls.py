"""
List of all the databse routes...
"""
from django.contrib import admin
from django.urls import path
from database import users
from database import subscription

urlpatterns = [
    path("addSub/", subscription.add_sub),
    path("getSub/", subscription.get_sub),
]
