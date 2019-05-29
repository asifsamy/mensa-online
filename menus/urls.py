from django.urls import path

from . import views

app_name = 'menus'
urlpatterns = [
    path('', views.MenuView.as_view(), name="menu"),
    #path('menu/', views.MenuView.as_view(), name="menu"),
    # path('add-menu/', views.AddMenuView.as_view(), name="add-menu"),
]