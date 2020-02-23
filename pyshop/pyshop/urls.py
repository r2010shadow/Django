"""pyshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path
from . import views as pviews
from books import views
from contact import views as cviews
from django.conf import settings


urlpatterns = [
    path('hello/',  pviews.hello),
    path('time/',   pviews.current_datetime),
    path('admin/',  admin.site.urls),
    path('t/t/',    pviews.current_datetime),
    re_path(r'time/plus/(\d{1,2})/',  pviews.hours_ahead),
    re_path(r'search-form/', views.search_form),
    re_path(r'search/',views.search),
    #re_path(r'contact/', views.contact),
    #re_path(r'contact_succ/', cviews.contact_succ),
    re_path(r'contact/',cviews.contact),
    re_path(r'contact/thanks/', cviews.contact_succ),
]
