from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('dashboard/', include('Dashboard.urls')),
    path('posts/', include('Posts.urls')),
    path('users/', include('Users.urls')),
    path('blog/', include('Blog.urls')),
    path('accounts/', include('Accounts.urls')),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)