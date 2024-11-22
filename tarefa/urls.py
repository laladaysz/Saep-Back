from django.urls import path
from . import views

urlpatterns = [
    path('tarefa/criar/', views.criar_tarefa, name='criar_tarefa'),
     path('tarefa/todas/', views.get_all_tarefas, name='get_all_tarefas'),
]
