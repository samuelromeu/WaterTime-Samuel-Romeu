from django.contrib import admin
from django.urls import path, include

from . import views 

urlpatterns = [
    path('', views.get_usuario, name='get_all_usuarios'),
    path('post/', views.post_usuario, name='post_usuario'),
    path('put/<int:pk>/', views.put_usuario, name='put_usuario'),
]

