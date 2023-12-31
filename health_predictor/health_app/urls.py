from django.urls import path
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('alzheimers/', views.alzheimers, name="alzheimers"),
  
]