from django.views.generic import ListView

from . models import Menu

# Create your views here.

class MenuView(ListView):
    template_name = "admin_temp/menu/menu.html"
    model = Menu

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set

class AddMenuView(ListView):
    template_name = "admin_temp/menu/add-menu.html"
    model = Menu

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set