from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome
