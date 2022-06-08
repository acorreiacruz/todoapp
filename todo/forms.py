from django import forms
from .models import Tarefa


class Cadastrar(forms.ModelForm):

    title = forms.CharField(
        max_length=150,
        min_length=10,
        label='Título da Tarefa',
        label_suffix=':',
        help_text='Ensira o título para a sua tarefa',
        error_messages={
            'required': 'Por favor insira um título para a tarefa'
        },
    )

    done = forms.BooleanField(
        label='Feito',
        label_suffix=':',
        help_text='Verdadeiro ou falso, se a tarefa já foi feita ou não',
        error_messages={
            'required': 'Este campo é obrigatório, escolha uma opção'
        }
    )

    class Meta:
        model = Tarefa
        fields = ['title', 'description']
