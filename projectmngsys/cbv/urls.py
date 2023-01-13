from django.contrib import admin
from django.urls import path,include
from .views import CreatePost,ListAllPost,PostDetail,PostDelete,UpdatePost

urlpatterns = [
 
    path('create/',CreatePost.as_view(),name='create'),
    path('list/',ListAllPost.as_view(),name='list'),
    path('detail/<int:pk>',PostDetail.as_view(),name='detail'),
    path('delete/<int:pk>',PostDelete.as_view(),name='delete'),
    path('update/<int:pk>',UpdatePost.as_view(),name='update')
]