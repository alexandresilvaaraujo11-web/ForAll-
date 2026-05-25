from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required 
from .models import Mensagem, Sala

from forum.models import Projeto


@login_required
def chat_sala(request, sala_id):
    #puxar projeto pra enviar o nome dele
    projeto = get_object_or_404(Projeto, id=sala_id)


    sala, criada = Sala.objects.get_or_create(
        id =sala_id,
        defaults={'nome': f'{projeto.titulo}'}    
    )


    if request.user not in sala.participantes.all():
        sala.participantes.add(request.user)
        # gerar mensagem de que ele entrou no grupo para o futuro se voltar a mexer

        Mensagem.objects.create(
            sala=sala,
            autor=request.user,
            texto=f'{request.user.username} entrou no grupo',
            sistema=True

        )

    if request.method == 'POST':
        texto = request.POST.get('texto')

        if texto: #não envia msg vazia

            Mensagem.objects.create(
                sala = sala,
                autor  = request.user,
                texto=texto
        )

        return redirect('chat:chat_sala', sala_id=sala.id)

    mensagens = sala.mensagens.all().order_by('-data')

    return render(request, 'chat.html', {
        'sala_id': sala_id,
        'sala': sala,
        'mensagens': mensagens
    })
