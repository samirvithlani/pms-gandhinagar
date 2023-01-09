from django.contrib import admin
from django.urls import path,include
from .views import CreatePost

urlpatterns = [
 
    path('create/',CreatePost.as_view(),name='create')
]