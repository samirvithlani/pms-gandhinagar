from django.contrib import admin
from django.urls import path
from .views import TeacherSignUpView,LoginView,StudentSignUpView
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('teachersignup/',TeacherSignUpView.as_view(),name='teachersignup'),
    path('studentsignup/',StudentSignUpView.as_view(),name='studentsignup'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout')
]
