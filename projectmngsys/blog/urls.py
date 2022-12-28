from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index),
    path('aboutus/',views.aboutus),
    path('contactus/',views.contactus),
    path('get/',views.getAllData),
    path('ques/',views.que_ans_vote),
    path('create/',views.creatOrm),
    path('delete/',views.deleteRecord),
    
]
