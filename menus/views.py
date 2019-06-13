from django.views.generic import ListView

from menus.models import Menu

# Added by FCO to use REST API
from menus.serializers import MenuSerializer
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
# Allow permission to any 
from rest_framework.permissions import AllowAny
@permission_classes((AllowAny, ))

# Create your views here.

class MenuViewSet(viewsets.ModelViewSet):
    """
    Add comments here
    """
    # authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Menu.objects.all() #Select Menu
    serializer_class = MenuSerializer #Serelize data

# Class below commented to use the class above with the API

# class MenuView(ListView):
#     template_name = "admin_temp/menu/menu.html"
#     model = Menu

#     def get_queryset(self):
#         query_set = super().get_queryset()
#         return query_set

class AddMenuView(ListView):
    template_name = "admin_temp/menu/add-menu.html"
    model = Menu

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set