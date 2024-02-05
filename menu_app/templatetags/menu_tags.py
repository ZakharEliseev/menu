from django import template
from menu_app.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu_app/menu.html')
def draw_menu(menu, current_path):
    return {'menu': menu, 'current_path': current_path}
