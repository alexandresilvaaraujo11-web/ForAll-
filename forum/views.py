from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Projeto
from .forms import ForumForm
from profiles.models import Cursos
from chat.models import Sala


def lista_projetos(request):

    projetos = Projeto.objects.all().order_by('-criado_em')
    for p in projetos:
        try:
            sala = Sala.objects.get(id=p.id)
            # Sobrescrevemos o valor do banco com a quantidade real do chat
            p.participantes_qtd = sala.participantes.count()
        except Sala.DoesNotExist:
            # Se ninguém abriu o chat ainda, o padrão é 1 (o próprio criador)
            p.participantes_qtd = 1

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
            cursos_selecionados = form.cleaned_data.get('curso')
            if cursos_selecionados:
                projeto.curso.set(cursos_selecionados) #salva as alterações do curso selecionavel
            messages.success(request, 'Projeto criado com sucesso!')
            return redirect('lista_projetos')
    else:
        form =ForumForm()

    template_name = 'form_forum.html'
    context = {
        'form': form,
        }
    return render(request, template_name, context)


def delete_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    projeto.delete()
    return redirect('lista_projetos') 
