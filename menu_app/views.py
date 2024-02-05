from django.shortcuts import render
from menu_app.models import MenuItem


# Create your views here.
def index_view(request, menu_name=None):
    if menu_name:
        menus = MenuItem.objects.filter(title=menu_name)
    else:
        menus = MenuItem.objects.all()
    current_path = request.path
    return render(request, 'cite/index.html', {'menus': menus, 'current_path': current_path})
