__author__ = 'zhangqiang'
from django.shortcuts import HttpResponse,redirect
from django.utils.deprecation import MiddlewareMixin
import re



class PermissionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # 取得当前的url用于和sesion中的进行比对
        current_url = request.path_info

        white_url = ['/app01/login', '/app01/register', '/admin/.*']
        for url in white_url:
            my_url = re.match(url, current_url)
            if my_url:
                # 返回空就不会继续走后面的代码了
                return None

        # 判断用户是否登录使用前面session中的user_id
        user_id = request.session.get('user_id')
        if not user_id:
            return redirect('/app01/login/')



        # 从session取出url列表
        permissions_list = request.session.get('permission_list')
        print("ttt permissions_list:%s" % permissions_list)
        """
        {
            3: {'url': ['/app01/role', '/app01/role/edit(\\d+)/', '/app01/delete/(\\d+)'], 'action': ['list', 'edit', 'delete']},
            4: {'url': ['/app01/add/user', '/app01/user', '/app01/delete/user', '/app01/edit/user'], 'action': ['add', 'list', 'delete', 'edit']}
        }
        """


        # 状态转换阀
        trance = False
        for i in permissions_list.values():
             for url in i.get('url'):
                url = '^{}$'.format(url)
                print(url)
                tf = re.match(url, current_url)
                if tf:
                    request.action = i.get('action')
                    return None

        if not trance:
            return HttpResponse('你没有权限访问！！！')
