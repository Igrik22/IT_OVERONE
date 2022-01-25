from django.urls import path

from core import views

urlpatterns = [
    path('resize-picture/', views.resize_picture, name='resized'),
]
