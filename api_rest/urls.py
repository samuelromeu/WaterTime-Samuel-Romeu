from django.contrib import admin
from django.urls import path, include

from . import views 

urlpatterns = [
    path('usuario', views.get_usuario, name='get_all_usuarios'),
    path('usuario/<int:pk>', views.get_usuario_by_id, name='get_usuario'),
    path('usuario/post', views.post_usuario, name='post_usuario'),
    path('usuario/put/<int:pk>/', views.put_usuario, name='put_usuario'),
    path('usuario/delete/<int:pk>/', views.delete_usuario, name='delete_usuario'),
    path('lembrete', views.get_lembrete, name='get_lembrete'),
    path('lembrete/<int:pk>', views.get_lembrete_by_id, name='get_lembrete'),
    path('lembrete/post', views.post_lembrete, name='post_lembrete'),
    path('lembrete/put/<int:pk>/', views.put_lembrete, name='put_lembrete'),
    path('lembrete/criar', views.criar_lembretes, name='criar_lembretes'),

]

