from django.db import migrations


def criar_cursos(apps, schema_editor):
    Cursos = apps.get_model('profiles', 'Cursos')

    for nome in [
        "Administração",
        "Arquitetura e Urbanismo",
        "Educação Física",
        "Biomedicina",
        "Direito",
        "Enfermagem",
        "Engenharia Civil",
        "Engenharia de Produção",
        "Engenharia de Software",
        "Engenharia Elétrica",
        "Engenharia Mecânica",
        "Engenharia Ambiental e Sanitária",
        "Fonoaudiologia",
        "Gestão em Recursos Humanos",
        "Logística",
        "Ciências Biológicas",
        "História",
        "Letras",
        "Matemática",
        "Pedagogia",
        "Nutrição",
        "Psicologia",
        "Serviço Social",
        "Sistemas de Informação",
        "Terapia Ocupacional",
        "Medicina",
    ]:
        Cursos.objects.get_or_create(curso=nome)


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_cursos_curso_alter_profile_bio_and_more'),
    ]

    operations = [
        migrations.RunPython(criar_cursos),
    ]