from django.db import models
from django.contrib.auth.models import AbstractUser 

class Cursos(models.Model):
    curso = models.CharField('Curso', max_length=200, default=0)

    def __str__(self):
        return self.curso

class Profile(AbstractUser):
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, verbose_name='Curso', blank=True, null=True)
    bio = models.TextField('Bio', max_length=500, default="")

    def __str__(self):
        return self.username

