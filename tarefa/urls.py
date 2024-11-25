from django.urls import path
from . import views

urlpatterns = [
    path('tarefa/criar/', views.criar_tarefa, name='criar_tarefa'),
    path('tarefa/todas/', views.get_all_tarefas, name='get_all_tarefas'),
    path('tarefa/alterar_status/<int:id>/', views.update_status, name='alterar_status'),   
    path('tarefa/excluir/<int:pk>/', views.excluir_tarefa, name='excluir_tarefa'),
    path('tarefa/alterar/<int:pk>/', views.atualizar_tarefa, name='atualizar_tarefa'),    
]
