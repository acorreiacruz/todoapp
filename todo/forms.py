from django import forms
from .models import Tarefa


class Cadastrar(forms.ModelForm):

    title = forms.CharField(
        max_length=150,
        min_length=4,
        label='Título da Tarefa',
        label_suffix=':',
        help_text='Insira o título para a sua tarefa',
        error_messages={
            'required': 'Campo obrigatório, por favor insira um título para\
            a tarefa',
            'max_length': 'O título pode ter no máximo 150 caracteres',
            'min_length': 'O título deve ter no mínimo 4 caracteres',
        },
        widget=forms.TextInput(attrs={
            'placeholder': 'Ex.: Minha Tarefa',
        }),
    )

    description = forms.CharField(
        max_length=300,
        min_length=4,
        label='Descrição',
        label_suffix=':',
        help_text='Escreva a descrição da tarefa',
        error_messages={
            'required': 'Campo obrigatório, por favor insira uma descrição para\
            a tarefa',
            'max_length': 'A descrição pode ter no máximo 300 caracteres',
            'min_length': 'A descrição deve ter no mínimo 4 caracteres',
        },
        widget=forms.Textarea(attrs={
            'placeholder': 'Ex.: Escreva uma descrição detalhada da tarefa de\
            até 300 caracteres!',
        })
    )

    class Meta:
        model = Tarefa
        fields = ['title', 'description']
