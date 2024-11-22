from django.urls import path
from . import views

urlpatterns = [
    path('tarefa/criar/', views.criar_tarefa, name='criar_tarefa'),
    
]
