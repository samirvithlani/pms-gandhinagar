from django.contrib import admin
from django.urls import path
from .views import TeacherSignUpView,LoginView,StudentSignUpView,CreateEletronicsWithFile,AddDocument,GetEletronics
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [

    path('teachersignup/',TeacherSignUpView.as_view(),name='teachersignup'),
    path('studentsignup/',StudentSignUpView.as_view(),name='studentsignup'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('sendmail/',views.sendMail,name='sendmail'),
    path('upload/',views.upload,name='upload'),
    path('upload1/',views.CreateEletronicsWithFile.as_view(),name='upload1'),
    path('upload2/',views.AddDocument.as_view(),name='upload2'),
    path('list/',views.GetEletronics.as_view(),name='list'),
    
]
