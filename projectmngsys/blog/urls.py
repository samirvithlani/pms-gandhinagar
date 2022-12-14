from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index),
    path('aboutus/',views.aboutus),
    path('contactus/',views.contactus),
]
