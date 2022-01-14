__author__ = 'zhangqiang'

from django.shortcuts import render, HttpResponse, redirect


def initial_permission(request, user_obj):
    # 把 user的id放入session
    request.session['user_id'] = user_obj.pk
    # 获取的角色相关的query
    role_obj = user_obj.roles.all()
    # 跨三个表查询到权限相关东西放在列表中
    permission_item = role_obj.values('permission__action', 'permission__url', 'permission__group__id')
    print("dddd permission_item:%s" % permission_item)
    """
    <QuerySet [
    {'permission__action': 'list', 'permission__url': '/app01/role', 'permission__group__id': 3},
    {'permission__action': 'edit', 'permission__url': '/app01/role/edit(\\d+)/', 'permission__group__id': 3},
    {'permission__action': 'delete', 'permission__url': '/app01/delete/(\\d+)', 'permission__group__id': 3},
    {'permission__action': 'add', 'permission__url': '/app01/add/user', 'permission__group__id': 4},
    {'permission__action': 'list', 'permission__url': '/app01/user', 'permission__group__id': 4},
    {'permission__action': 'delete', 'permission__url': '/app01/delete/user', 'permission__group__id': 4},
    {'permission__action': 'edit', 'permission__url': '/app01/edit/user', 'permission__group__id': 4}
    ]>
    """


    # 构建一个新的字典储存提取到的权限相关东西
    permission_list = {}
    for i in permission_item:
        if i.get('permission__group__id') not in permission_list.keys():
            permission_list[i.get('permission__group__id')] = {
                'url': [i.get('permission__url'), ],
                'action': [i.get('permission__action'), ]
            }
        else:
            permission_list[i.get('permission__group__id')]['url'].append(i.get('permission__url'))
            permission_list[i.get('permission__group__id')]['action'].append(i.get('permission__action'))

    # 将获取的权限相关存储到session中
    print("zzz permission_list:%s" % permission_list)
    """
    {
        3: {'url': ['/app01/role', '/app01/role/edit(\\d+)/', '/app01/delete/(\\d+)'], 'action': ['list', 'edit', 'delete']},
        4: {'url': ['/app01/add/user', '/app01/user', '/app01/delete/user', '/app01/edit/user'], 'action': ['add', 'list', 'delete', 'edit']}
    }
    """
    request.session['permission_list'] = permission_list


    # menu显示，至少需要url，title字段
    action_dict = role_obj.values('permission__action', 'permission__url', 'permission__group__title').distinct()
    print("action_dict：%s" % action_dict)
    """
    <QuerySet [
    {'permission__action': 'list', 'permission__url': '/app01/role', 'permission__group__title': '角色管理'},
    {'permission__action': 'edit', 'permission__url': '/app01/role/edit(\\d+)/', 'permission__group__title': '角色管理'},
    {'permission__action': 'delete', 'permission__url': '/app01/delete/(\\d+)', 'permission__group__title': '角色管理'},
    {'permission__action': 'add', 'permission__url': '/app01/add/user', 'permission__group__title': '用户管理'},
    {'permission__action': 'list', 'permission__url': '/app01/user', 'permission__group__title': '用户管理'},
    {'permission__action': 'delete', 'permission__url': '/app01/delete/user', 'permission__group__title': '用户管理'},
    {'permission__action': 'edit', 'permission__url': '/app01/edit/user', 'permission__group__title': '用户管理'}
    ]>
    """
    action_list = []
    for i in action_dict:
        if i.get("permission__action") == 'list':
            action_list.append((i.get('permission__url'), i.get('permission__group__title')))

    print("action_list:%s" % action_list)
    """
    [
        ('/app01/role', '角色管理'),
        ('/app01/user', '用户管理')
    ]
    """
    # 把提取出的url放入session中  [('/user/', '用户管理')]
    request.session['action_list'] = action_list




