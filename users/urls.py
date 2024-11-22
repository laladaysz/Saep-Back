from django.urls import path
from . import views

urlpatterns = [
    path('users/cadastro/', views.cadastro, name='cadastro'),
    path('users/', views.get_all_users, name='get_all_users'),
    path('users/<int:id>/', views.get_user_by_id, name='get_user_by_id')

]
