from django.contrib import admin
from django.urls import path, include
from homeApp import views
urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.handleLogin, name="Login"),
    path('signin', views.handleSignin, name="signin"),
    path('logout', views.handleLogout, name="logout"),
]
