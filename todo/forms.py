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
        widget=forms.TextInput(attrs={
            'placeholder': 'Ex.: Minha Tarefa',
        }),
    )

    description = forms.CharField(
        max_length=300,
        label='Descrição',
        label_suffix=':',
        help_text='Escreva a descrição da tarefa',
        error_messages={
            'required': 'Por favor, insira uma descrição para a tarefa',
        },
        widget=forms.Textarea(attrs={
            'placeholder': 'Ex.: Aqui vai uma descrição detalhada da tarefa!',
        })
    )

    done = forms.BooleanField(
        label='Tarefa já foi feita ?',
        label_suffix=':',
        help_text='Check -> já concluída | Uncheck -> não concluída',
        error_messages={
            'required': 'Este campo é obrigatório, escolha uma opção'
        },
    )

    class Meta:
        model = Tarefa
        fields = ['title', 'description']
