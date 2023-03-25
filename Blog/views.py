from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# blog index
def index(request):
    dict = {'insert_me': "Hello I am from views.py!"}
    return render(request, 'Blog/blogs.html', context=dict)