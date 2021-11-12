__author__ = 'zhangqiang'

from django.shortcuts import render, HttpResponse, redirect


def initial_permission(request, user_obj):
    # �� user��id����session
    request.session['user_id'] = user_obj.pk

    # �����Ȱ��û���Ӧ��ӵ�е�url���ȡ���ŵ�session�б��ã�ͨ��user_obj���role�ٵ�permission�õ�url��
    role_obj = user_obj.roles.all()
    url_list = role_obj.values('permission__url')  # ȡ����url��queryset���� <QuerySet [{'permissions__url': '/user/'}, {'permissions__url': '/add/user/'}, {'permissions__url': '/role/'}]>

    permission_list = []
    for i in url_list:
        permission_list.append(i['permission__url'])
    print("login permission_list:%s" % permission_list)

    request.session['permissions_list'] = permission_list

