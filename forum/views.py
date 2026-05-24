from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Projeto
from .forms import ForumForm



def lista_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'forum/lista.html',{'projetos': projetos})

@login_required
def novo_projeto(request):
    
    if request.method == 'POST':
        form = ForumForm(request.POST)
        if form.is_valid():
            projeto=form.save(commit=False)
            projeto.criador = request.user
            projeto.save()
        return redirect('lista_projetos')
    else:
        template_name = 'form_forum.html'
        context = {
            'form': ForumForm(),
        }
        return render(request, template_name, context)


def delete_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    projeto.delete()
    return redirect('lista_projetos') 
