from django.urls import path
from app_bloco_notas import views

app_name = "notas"

urlpatterns = [
    path('', views.home, name='home'),

    path('adicionar/', views.adicionar_notas, name='adicionar'),
    path('remover/<int:id>', views.remover_notas, name='remover'),
    path('editar/<int:id>', views.editar_notas, name='editar')
]