"""
List of all the databse routes...
"""
from django.contrib import admin
from django.urls import path
from database import users
from database import subscription
from database import bus_services

urlpatterns = [
    path("addSub/", subscription.add_sub),
    path("getSub/", subscription.get_sub),
    path("getBusSchedule/", bus_services.get_bus_schedule),
]
