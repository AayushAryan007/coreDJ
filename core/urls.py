"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home.views import *
from vege.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name='home'),
    path('about/', about_page, name='about'),
    path('contact/', contact_page, name='contact'),
    path('success/', success_page, name='success'),
    path('admin/', admin.site.urls),
    path('receipes/', receipes, name='receipes'),
    path('edit-recipe/<int:recipe_id>/', edit_recipe, name='edit_recipe'),
    path('delete-recipe/<int:recipe_id>/', delete_recipe, name='delete_recipe'),

    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
