__author__ = 'zhangqiang'


from django.contrib import admin


from django.urls import path
from app01.views import login,add_user,user,role

urlpatterns = [
    path('login', login, name='login'),
    path('add/user', add_user, name='add_user'),
    path('user', user, name='user'),
    path('role', role, name='role')

]