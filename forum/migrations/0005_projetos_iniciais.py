from django.db import migrations
from django.contrib.auth.hashers import make_password


def criar_dados_iniciais(apps, schema_editor):
    Cursos = apps.get_model('profiles', 'Cursos')
    Profile = apps.get_model('profiles', 'Profile')
    Projeto = apps.get_model('forum', 'Projeto')

    demo_user, _ = Profile.objects.get_or_create(
        username='demo',
        defaults={
            'email': 'demo@forall.com',
            'password': make_password('demo123')
        }
    )

    hackathon, _ = Projeto.objects.get_or_create(
        titulo='Hackathon UGB 2026',
        defaults={
            'descricao': 'Projeto de equipe para hackathon universitário 2026.',
            'criador': demo_user,
            'participantes_qtd': 5,
        }
    )

    forall_mobile, _ = Projeto.objects.get_or_create(
        titulo='ForAll Mobile',
        defaults={
            'descricao': 'Versão mobile da plataforma ForAll para estudantes.',
            'criador': demo_user,
            'participantes_qtd': 4,
        }
    )

    cursos = [
        'Sistemas de Informação',
        'Engenharia de Software',
        'Administração',
    ]

    for nome in cursos:
        try:
            c = Cursos.objects.get(curso=nome)
            hackathon.curso.add(c)
            forall_mobile.curso.add(c)
        except Cursos.DoesNotExist:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_adicionar_cursos_iniciais'),
        ('forum', '0004_remove_projeto_curso_projeto_curso'),
    ]

    operations = [
        migrations.RunPython(criar_dados_iniciais),
    ]