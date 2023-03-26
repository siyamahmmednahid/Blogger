from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='Accounts:signIn')
def Posts(request):
    return render(request, 'Posts/posts.html')
