from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login


# Create your views here.
def MyAccount(request):
    return render(request, 'Accounts/myAccount.html')

def SignUp(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'Accounts/myAccount.html')
    dict = {'form': form, 'title': 'Sign Up'}
    return render(request, 'Accounts/signUp.html', {'form': form})

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
                return render(request, 'Accounts/myAccount.html')
    dict = {'form': form, 'title': 'Sign In'}
    return render(request, 'Accounts/signIn.html', {'form': form})
