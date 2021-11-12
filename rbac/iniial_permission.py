__author__ = 'zhangqiang'

from django.shortcuts import render, HttpResponse, redirect


def initial_permission(request, user_obj):
    # 把 user的id放入session
    request.session['user_id'] = user_obj.pk

    # 我们先把用户对应的拥有的url添加取出放到session中备用（通过user_obj跨表到role再到permission拿到url）
    role_obj = user_obj.roles.all()
    url_list = role_obj.values('permission__url')  # 取出的url是queryset对象 <QuerySet [{'permissions__url': '/user/'}, {'permissions__url': '/add/user/'}, {'permissions__url': '/role/'}]>

    permission_list = []
    for i in url_list:
        permission_list.append(i['permission__url'])
    print("login permission_list:%s" % permission_list)

    request.session['permissions_list'] = permission_list

