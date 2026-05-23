from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileCreationForm

#   imports pra login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login

def register(request):
    if request.method == 'POST':
        form = ProfileCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        form = ProfileCreationForm()
    template_name = 'register.html'
    context = {
        'form':form
    }
    return render(request, template_name, context)

def login(request):
    if request.method == 'POST':
        # authentication form recebe o request e os dados separados

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            # Pegamos o usuário e senha digitado
            usuario = form.cleaned_data.get('username')
            senha = form.cleaned_data.get()

            # authenticate() vai no banco de dados e checa se tão correto
            user = authenticate(username=usuario, passwrod=senha)

            if user is not None:
                #auth login é oq loga
                auth_login(request, user)

                # para onde ele vai depois de logar?
                return redirect('profile:reg')
        else:
            form = AuthenticationForm()
        context = {
            'form':form
        }
        return render(request, 'login.html', context)

