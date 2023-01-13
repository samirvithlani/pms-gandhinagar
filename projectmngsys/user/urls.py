from django.contrib import admin
from django.urls import path
from .views import TeacherSignUpView

urlpatterns = [

    path('signup/',TeacherSignUpView.as_view(),name='teachersignup')    
]
