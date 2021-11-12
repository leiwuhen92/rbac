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
           return redirect('/app01/add/user')

        return render(request, 'login.html')

    return render(request, 'login.html')



def user(request):
    return HttpResponse('查看用户成功！！！')


def add_user(request):
    # import re
    # # 从session取出url列表
    # permissions_list = request.session.get('permissions_list')
    # print("add user permissions_list:%s" % permissions_list)
    #
    # # 取得当前的url用于和sesion中的进行比对
    # current_url = request.path_info
    # # 状态转换阀
    # trance = False
    # for i in permissions_list:
    #     # 进行前后限定。使其匹配准确度为百分百
    #     i = '^{0}$'.format(i)
    #     match = re.match(i, current_url)
    #     # 如果匹配成功，状态阀改为True，并跳出匹配
    #     if match:
    #         trance = True
    #         break
    #
    # # 根据状态阀来判断当前用户是否有访问权限
    # if not trance:
    #     return HttpResponse('你没有权限访问！！！')

    return HttpResponse('添加用户成功！！！')



def role(request):
    return HttpResponse('查看角色成功！！！')

