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
@login_required
def chat_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    # Garante que a sala exista
    sala, criada = Sala.objects.get_or_create(id=projeto.id, defaults={'nome': projeto.titulo})
    
    mensagens = sala.mensagens.all().order_by('data')
    
    if request.method == 'POST':
        texto = request.POST.get('texto', '').strip()
        if texto:
            sala.mensagens.create(autor=request.user, texto=texto)
            return redirect('chat_projeto', projeto_id=projeto.id)
            
    return render(request, 'chat.html', {
        'projeto': projeto,
        'sala': sala,            
        'mensagens': mensagens
    })

@login_required
def update_projeto(request, projeto_id):
    
    projeto = get_object_or_404(Projeto, id=projeto_id)
    
    #Garante que apenas o criador possa editar o próprio projeto
    if projeto.criador != request.user:
        messages.error(request, 'Você não tem permissão para editar este projeto.')
        return redirect('lista_projetos')

    if request.method == 'POST':
        # 2. Passamos o request.POST e a 'instance=projeto' para o Django saber que é uma ATUALIZAÇÃO
        form = ForumForm(request.POST, instance=projeto)
        
        if form.is_valid():
            # Salva os dados de texto (titulo, descricao, etc.)
            projeto = form.save(commit=False)
            projeto.save()
            
            # 3. Atualiza as relações ManyToMany (Cursos)
            cursos_selecionados = form.cleaned_data.get('curso')
            if cursos_selecionados:
                projeto.curso.set(cursos_selecionados)
            else:
                projeto.curso.clear() # Se ele desmarcar tudo, limpa as relações
                
            messages.success(request, 'Projeto atualizado com sucesso!')
            return redirect('lista_projetos')
    else:
        form = ForumForm(instance=projeto)
    
    template_name = 'form_forum.html'
    context = {
        'form': form,
        'projeto': projeto, # Passamos o projeto para o HTML saber se é uma edição ou criação
    }
    return render(request, template_name, context)

def detalhe_projeto (request,pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    return render(request,'forum/detalhe_projeto.html', {'projeto': projeto})