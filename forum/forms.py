from django.forms import ModelForm,CheckboxSelectMultiple
from .models import Projeto

class ForumForm (ModelForm):
    class Meta:
        model = Projeto
        fields = ['curso','titulo','descricao','participantes_qtd']

        widgets = {
            'cursos':CheckboxSelectMultiple(),
        }