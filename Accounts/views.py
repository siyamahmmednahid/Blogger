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
                return HttpResponseRedirect(reverse('Dashboard:dashboard'))
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



# Add Profile Pic
@login_required(login_url='Accounts:signIn')
def AddProfilePic(request):
    form = forms.ProfilePicForm()
    if request.method == 'POST':
        form = forms.ProfilePicForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect(reverse('Accounts:myAccount'))
    dict = {'form': form, 'title': 'Add Profile Pic'}
    return render(request, 'Accounts/addProfilePic.html', {'form': form})



# Change Profile Pic
@login_required(login_url='Accounts:signIn')
def ChangeProfilePic(request):
    form = forms.ProfilePicForm(instance=request.user.Profile_Pic)
    if request.method == 'POST':
        form = forms.ProfilePicForm(request.POST, request.FILES, instance=request.user.Profile_Pic)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Accounts:myAccount'))
    dict = {'form': form, 'title': 'Edit Profile Pic'}
    return render(request, 'Accounts/addProfilePic.html', {'form': form})



# Delete Profile Pic
@login_required(login_url='Accounts:signIn')
def DeleteProfilePic(request):
    request.user.Profile_Pic.delete()
    return HttpResponseRedirect(reverse('Accounts:myAccount'))