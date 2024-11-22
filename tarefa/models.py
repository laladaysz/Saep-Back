from django.db import models
from users.models import User  

class Tarefa(models.Model):
    id = models.AutoField(primary_key=True)  
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tarefas')  
    titulo = models.CharField(max_length=45)  
    descricao = models.CharField(max_length=100)  
    setor = models.CharField(max_length=45)  
    prioridade = models.CharField(max_length=45)  
    data_cadastro = models.DateTimeField(auto_now_add=True)  
    status = models.CharField(max_length=45)  
    
    def __str__(self):
        return self.titulo
