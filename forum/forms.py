from django.forms import ModelForm
from .models import Projeto

class ForumForm (ModelForm):
    class Meta:
        model = Projeto
        fields = ['curso','titulo','descricao','criador','participantes_qtd']