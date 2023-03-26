from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . import forms



# Sign Up
def SignUp(request):
    form = forms.SignUpForm()
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Accounts:myAccount'))
    dict = {'form': form, 'title': 'Sign Up'}
    return render(request, 'Accounts/signUp.html', {'form': form})



# Sign In
def SignIn(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('Accounts:myAccount'))
    dict = {'form': form, 'title': 'Sign In'}
    return render(request, 'Accounts/signIn.html', {'form': form})



# Sign Out
@login_required(login_url='Accounts:signIn')
def SignOut(request):
    logout(request)
    return HttpResponseRedirect(reverse('Accounts:myAccount'))



# My Account
@login_required(login_url='Accounts:signIn')
def MyAccount(request):
    return render(request, 'Accounts/myAccount.html')