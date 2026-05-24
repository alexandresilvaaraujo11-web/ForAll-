from django.db import models
from django.conf import settings
from profiles.models import Cursos

class Projeto(models.Model):
    curso = models.ManyToManyField(Cursos, related_name='projetos',verbose_name='Cursos do Projeto')
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    criador=models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='projetos'
    )
    participantes_qtd = models.IntegerField(default=1)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo 