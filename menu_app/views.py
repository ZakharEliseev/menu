from django.db.models import F
from django.shortcuts import render
from menu_app.models import MenuItem


# Create your views here.
def index_view(request, menu_name=None):
    if menu_name:
        menu = MenuItem.objects.get(title=menu_name)
        menus = menu.get_descendants(include_self=True)
    else:
        menus = MenuItem.objects.all()

    current_path = request.path
    return render(request, 'cite/index.html', {'menus': menus, 'current_path': current_path})
