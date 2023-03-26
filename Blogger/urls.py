from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('dashboard/', include('Dashboard.urls')),
    path('posts/', include('Posts.urls')),
    path('users/', include('Users.urls')),
    path('blog/', include('Blog.urls')),
    path('accounts/', include('Accounts.urls')),
]
