from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.models import User
from django.shortcuts import render
from .views import  HomeView



urlpatterns = [

    path('', views.HomeView, name='home'),

]
