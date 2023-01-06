from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
 
 path('add/',views.employee_create_view,name='addemployee'),
 path('list/',views.employee_list_view,name='listemployee'),
 path('delete/<int:id>',views.employee_delete_view,name='deleteemployee'),
 path('detail/<int:id>',views.employee_detail_view,name='detailemployee'),
 path('update/<int:id>',views.employee_update_view,name='updateemployee')
 
]