from django.db import models

class Mensagem(models.Model):
    nome = models.CharField(max_length=100)
    texto = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome