from django.shortcuts import render, redirect
from .models import Mensagem

def chat(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        texto = request.POST.get('texto')

        Mensagem.objects.create(
            nome=nome,
            texto=texto
        )

        return redirect('chat')

    mensagens = Mensagem.objects.all().order_by('-data')

    return render(request, 'chat.html', {
        'mensagens': mensagens
    })
