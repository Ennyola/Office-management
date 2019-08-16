from django.contrib import admin
from django.urls import path,include
from . import views


app_name = 'office'
urlpatterns = [
    
     path('signup/', views.createuser, name = "createuser"),
     path('init_login/', views.init_login, name = "init_login"),
     path('login/', views.login_view, name = "login"),
     path('user_details/', views.user_details, name = "user_details"),
     path('logout/', views.logout_view, name = "logout"),
     path('status/', views.status, name = "status"),
     path('change_details/', views.change_details, name = "change"),
     path('init_details/', views.init_details, name = "init_details" ),
     path('my_info/', views.my_info, name = "my_info"),
     path('all_staff/', views.all_staff, name = "all_staff"),
    
]