from django.urls import path,re_path
from kingadmin import views


urlpatterns = [
    re_path(r'^$', views.app_index, name='app_index'),
    path('king_login/', views.acc_login, name='king_login'),
    path('king_logout/', views.acc_logout, name='king_logout'),
    re_path(r'^(\w+)/(\w+)/$', views.table_obj_list,name='table_obj_list'),
    re_path(r'^(\w+)/(\w+)/(\d+)/change/$', views.table_obj_change,name='table_obj_change'),
    re_path(r'^(\w+)/(\w+)/add/$', views.table_obj_add,name='table_obj_add'),
]