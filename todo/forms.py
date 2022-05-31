from django import forms
from .models import Tarefa


class Cadastrar(forms.ModelForm):


    class Meta:
        model = Tarefa
        fields = ['title', 'description']
    