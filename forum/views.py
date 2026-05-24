from django.shortcuts import render, redirect
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Projeto
from .forms import ForumForm



def lista_projetos(request):

    projetos = Projeto.objects.all()

    termo = request.GET.get('q', '').strip()
    curso_selecionado = request.GET.get('curso', '').strip()

    # pesquisa
    if termo:
        projetos = projetos.filter(
            titulo__icontains=termo
        ) | projetos.filter(
            descricao__icontains=termo
        ) | projetos.filter(
            criador_nome__icontains=termo
        )

    # filtro
    if curso_selecionado:
        projetos = projetos.filter(
            curso=curso_selecionado
        )

    cursos = Projeto.objects.values_list(
        'curso',
        flat=True
    ).distinct()

    return render(request, 'forum/lista.html', {
        'projetos': projetos,
        'cursos': cursos,
        'termo': termo,
        'curso_selecionado': curso_selecionado,
    })

@login_required
def novo_projeto(request):
    
    if request.method == 'POST':
        form = ForumForm(request.POST)
        if form.is_valid():
            projeto=form.save(commit=False)
            projeto.criador = request.user
            projeto.save()
        messages.success(request, 'Projeto criado com sucesso!')
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

@login_required 
def deletar_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    if projeto.criador != request.user:
        messages.error(request, "Você não tem permissão para deletar este projeto.")
        return redirect('lista_projetos')     
    if request.method == 'POST':
        projeto.delete()
        messages.success(request, "Projeto deletado com sucesso!") 
    return redirect('lista_projetos')
