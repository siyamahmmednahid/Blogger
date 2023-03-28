from django.urls import path
from . import views


app_name = 'Accounts'

urlpatterns = [
    path('', views.MyAccount, name='myAccount'),
    path('signin/', views.SignIn, name='signIn'),
    path('signup/', views.SignUp, name='signUp'),
    path('signout/', views.SignOut, name='signOut'),
    path('addprofilepic/', views.AddProfilePic, name='addProfilePic'),
    path('changeprofilepic/', views.ChangeProfilePic, name='changeProfilePic'),
    path('deleteprofilepic/', views.DeleteProfilePic, name='deleteProfilePic'),
]