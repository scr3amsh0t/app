"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('groups/', views.groups, name='groups'),
    path('account/', views.account, name='account'),
    path('handle_posts/', views.handle_posts, name='handle_posts'),
    path('handle_comments/', views.handle_comments, name='handle_comments'),
    path('handle_user_subs/', views.handle_user_subs, name='handle_user_subs'),
    path('handle_group_members/', views.handle_group_members, name='handle_group_members'),
]
