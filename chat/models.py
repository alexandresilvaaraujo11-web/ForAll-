from django.db import models
from django.conf import settings

class Sala(models.Model):
    # O nome ou título do grupo (ex: "Grupo de TCC", "Chat do Projeto X")
    nome = models.CharField(max_length=150)
    # blank=True permite que uma sala seja criada vazia no início
    participantes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='salas', blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nome

class Mensagem(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name='mensagens')
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    texto = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    sistema = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.autor.username} em {self.sala.nome}"