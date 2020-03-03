from django.urls import path,re_path
from kingadmin.views import acc_login,acc_logout,app_index,table_obj_list

urlpatterns = [
    re_path(r'^$', app_index, name='app_index'),
    path('king_login/', acc_login, name='king_login'),
    path('king_logout/', acc_logout, name='king_logout'),
    re_path(r'^(\w+)/(\w+)/$', table_obj_list,name='table_obj_list'),
]