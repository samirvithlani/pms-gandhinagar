from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
 
 path('add/',views.employee_create_view,name='add'),
 path('list/',views.employee_list_view,name='list'),
]