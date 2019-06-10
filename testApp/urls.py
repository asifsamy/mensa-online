"""
high level support for doing this and that.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from testApp import views

router = DefaultRouter()
router.register(r'notes', views.NoteViewSet)

urlpatterns = [
    path('', include(router.urls))
]