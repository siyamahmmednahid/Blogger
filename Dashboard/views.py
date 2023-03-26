from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='Accounts:signIn')
def Dashboard(request):
    return render(request, 'Dashboard/dashboard.html')