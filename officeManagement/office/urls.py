from django.contrib import admin
from django.urls import path
from . import views

app_name = 'office'
urlpatterns = [
    
    path('signup/', views.createuser, name = "createuser"),
    path('login/', views.login_view, name = "login"),
    path('user_details/', views.user_details, name = "user_details"),
    path('logout/', views.logout_view, name = "logout"),
    path('status/', views.status, name = "status"),
    path('change_details/', views.change_details, name = "change"),
    path('init_details/', views.init_details, name = "init_details" ),
    path('my_info/', views.my_info, name = "my_info")

]