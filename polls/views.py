from django.shortcuts import render
from django.template import loader
from django.http import Http404
from django.http import HttpResponse
from .models import Petition
from django.shortcuts import get_object_or_404, render
from .models import  Petition
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils import timezone
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required 

def HomeView(request):
    return render(request, 'polls/home.html')