from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from .models import Mensagem

@login_required
def chat(request):
    if request.method == 'POST':
        texto = request.POST.get('texto')

        if texto: #não envia msg vazia

            Mensagem.objects.create(
                autor  = request.user,
                texto=texto
        )

        return redirect('chat:chat')

    mensagens = Mensagem.objects.all().order_by('-data')

    return render(request, 'chat.html', {
        'mensagens': mensagens
    })
