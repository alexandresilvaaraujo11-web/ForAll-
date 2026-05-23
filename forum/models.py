from django.db import models

class Projeto(models.Model):
    curso = models.CharField(max_length=100)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    criador_nome = models.CharField(max_length=150)
    participantes_qtd = models.IntegerField(default=1)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo 