from django.forms import ModelForm,CheckboxSelectMultiple
from .models import Projeto
from profiles.models import Cursos
from django import forms

class ForumForm (ModelForm):
    curso = forms.ModelMultipleChoiceField(
        queryset=Cursos.objects.all(),
        widget=CheckboxSelectMultiple(),
        required=True, # <-- Isso impede o envio do formulário em branco
        label="Cursos do Projeto",
        error_messages={
            'required': 'Você precisa selecionar pelo menos um curso para criar o projeto.'}
    )

    class Meta:


        model = Projeto
        fields = ['curso','titulo','descricao','participantes_qtd']
