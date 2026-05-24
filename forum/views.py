from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Projeto
from .forms import ForumForm
from profiles.models import Cursos


def lista_projetos(request):

    projetos = Projeto.objects.all().order_by('-criado_em')

    termo = request.GET.get('q', '').strip()
    curso_selecionado = request.GET.get('curso', '').strip()

    # pesquisa
    if termo:
        projetos = projetos.filter(
            Q(titulo__icontains=termo) |
            Q(descricao__icontains=termo) |
            Q(criador__username__icontains=termo)
        ).distinct()

    # filtro
    if curso_selecionado:
        projetos = projetos.filter(
            curso__curso=curso_selecionado
        ).distinct()

    cursos = Cursos.objects.values_list(
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
            form.save_m2m() #salva as alterações do curso selecionavel
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
