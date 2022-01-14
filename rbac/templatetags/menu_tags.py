__author__ = 'zhangqiang'

from django import template

# 一定要是register这个名字
register = template.Library()

@register.inclusion_tag('menu.html')
def menu(request):
    action_list = request.session.get('action_list', [])
    return {'action_list': action_list}
