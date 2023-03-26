from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
def index(request):
    return HttpResponseRedirect(reverse('Blog:index'))