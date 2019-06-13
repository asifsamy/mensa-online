"""
Add comments here.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from menus import views

# New code to use  REST API

router = DefaultRouter()
router.register(r'menu', views.MenuViewSet)

urlpatterns = [
    path('', include(router.urls))
]

# Old code

# app_name = 'menus'
# urlpatterns = [
#     path('', views.MenuView.as_view(), name="menu"),
    #path('menu/', views.MenuView.as_view(), name="menu"),
    # path('add-menu/', views.AddMenuView.as_view(), name="add-menu"),
# ]

