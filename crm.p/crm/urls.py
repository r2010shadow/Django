from django.urls import path,re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.dashboard,name='sales_dashboard'),
]
