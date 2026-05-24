from django.db import models
from django.contrib.auth.models import AbstractUser 

class Cursos(models.Model):
    curso = models.CharField('Curso', max_length=200, default=0)

    def __str__(self):
        return self.curso

class Profile(AbstractUser):
    # ==========================================
    # CAMPOS NATIVOS DO DJANGO (Já vêm prontos)
    # ==========================================
    # username     (CharField)     -> Nome de usuário único (obrigatório por padrão)
    # first_name   (CharField)     -> Primeiro nome
    # last_name    (CharField)     -> Sobrenome
    # email        (EmailField)    -> E-mail do usuário
    # password     (CharField)     -> Senha (já vem criptografada com hash)
    # 
    # --- Status e Permissões ---
    # is_active    (BooleanField)  -> Se False, o usuário não consegue logar (banido/desativado)
    # is_staff     (BooleanField)  -> Se True, pode acessar esse painel do /admin
    # is_superuser (BooleanField)  -> Se True, tem poder absoluto sobre tudo
    # 
    # --- Datas Automáticas ---
    # last_login   (DateTimeField) -> Última vez que a pessoa fez login
    # date_joined  (DateTimeField) -> Data exata em que a conta foi criada
    # ==========================================

    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, verbose_name='Curso', blank=True, null=True)
    bio = models.TextField('Bio', max_length=500, default="")

    def __str__(self):
        return self.username

