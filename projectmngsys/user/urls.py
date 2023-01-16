from django.contrib import admin
from django.urls import path
from .views import TeacherSignUpView,LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('signup/',TeacherSignUpView.as_view(),name='teachersignup'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout')
]
