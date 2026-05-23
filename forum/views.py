from django.shortcuts import render
from .models import Projeto

def lista_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'forum/lista.html',{'projetos': projetos})
