from django.shortcuts import render, redirect
from .models import Projeto
from .forms import ForumForm

def lista_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'forum/lista.html',{'projetos': projetos})


def novo_projeto(request):
    
    if request.method == 'POST':
        form = ForumForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('forum:lista_projetos')
    else:
        template_name = 'form_produto.html'
        context = {
            'form': ForumForm(),
        }
        return render(request, template_name, context)


