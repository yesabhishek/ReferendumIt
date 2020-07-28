from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.models import User
from django.shortcuts import render
from .views import DetailView, ResultsView, HomeView



urlpatterns = [

    path('', HomeView.as_view(), name='home'), 
    path('<int:pk>/', DetailView.as_view(), name='details'),
    path('<int:pk>/result/', ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

]
