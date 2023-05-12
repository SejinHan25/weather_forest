from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path("",views.index,name="home"),
    path("auth/login",views.user_login,name="login"),
    path("auth/logout",views.user_logout, name="logout"),
    path("auth/signup",views.user_signup,name="signup"),
]
