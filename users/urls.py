from django.urls import path
from . import views

urlpatterns = [
    path('users/cadastro/', views.cadastro, name='cadastro'),
    
]
