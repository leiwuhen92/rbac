# Create your views here.

from django.shortcuts import render, HttpResponse, redirect
from rbac.iniial_permission import initial_permission
# Create your views here.
from rbac.models import *


def login(request):
    if request.method == "POST":
        user = request.POST.get('name')
        pwd = request.POST.get('pwd')

        user_obj = User.objects.filter(name=user, pwd=pwd).first()
        if user_obj:
           initial_permission(request, user_obj)
           return redirect('/app01/user')

        return render(request, 'login.html')

    return render(request, 'login.html')



#细粒度权限控制方法封装
class Per(object):
    def __init__(self, request):
        self.action = request.action

    def add(self):
        return 'add' in self.action

    def delete(self):
        return 'delete' in self.action

    def edit(self):
        return 'edit' in self.action

    def list(self):
        return 'list' in self.action


def user(request):
    user_obj = User.objects.all()
    per = Per(request)
    return render(request, 'user.html', {'user_obj': user_obj, 'per': per})


def add_user(request):
    return HttpResponse('添加用户成功！！！')



def role(request):
    user_obj = User.objects.all()
    role_obj = user_obj.values('name', 'role__title')
    print("role role_obj:%s" % role_obj)
    return render(request, 'role.html', {'role_obj': role_obj})


