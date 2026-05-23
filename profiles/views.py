from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileCreationForm

def reg(request):
    if request.method == 'POST':
        form = ProfileCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        form = ProfileCreationForm()
    template_name = 'reg.html'
    context = {
        'form':ProfileCreationForm()
    }
    return render(request, template_name, context)
