__author__ = 'zhangqiang'

from django import template

# һ��Ҫ��register�������
register = template.Library()

@register.inclusion_tag('menu.html')
def menu(request):
    action_list = request.session.get('action_list', [])
    return {'action_list': action_list}
