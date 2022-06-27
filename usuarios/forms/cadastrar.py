from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class CadastrarForm(forms.ModelForm):

    first_name = forms.CharField(
        required=True,
        min_length=3,
        max_length=50,
        label='Primeiro Nome',
        help_text='Digite o seu primeiro nome, utilizando de 3 a 50 caracteres',# noqa
        error_messages={
            'required': 'Campo obrigatório, por favor insira o seu primeiro nome!',# noqa
            'min_length': 'O primeiro nome deve ter no mínimo 3 caracteres',
            'max_length': 'O primeiro nome deve ter no máximo 50 caracteres',
        },
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ex.: Jhon'
            }
        )
    )

    last_name = forms.CharField(
        required=True,
        min_length=3,
        max_length=50,
        label='Último Nome',
        help_text='Digite o seu último nome, utilizando de 3 a 50 caracteres',
        error_messages={
            'required': 'Campo obrigatório, por favor insira o seu último nome!',# noqa
            'min_length': 'O último nome deve ter no mínimo 3 caracteres',
            'max_length': 'O último nome deve ter no máximo 50 caracteres',
        },
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ex.: Doe'
            }
        )
    )

    username = forms.CharField(
        required=True,
        min_length=3,
        max_length=50,
        label='Nome de Usuário',
        help_text='Digite o seu nome de usuário, utilizando de 3 a 50 caracteres',# noqa
        error_messages={
            'required': 'Campo obrigatório, por favor insira o seu nome de usuário!',# noqa
            'min_length': 'O nome de usuário deve ter no mínimo 3 caracteres',
            'max_length': 'O nome de usuário deve ter no máximo 50 caracteres',
        },
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ex.: jhondoe'
            }
        )
    )

    email = forms.CharField(
        required=True,
        label='E-mail',
        help_text='Insira um endereço de e-mail válido.',
        error_messages={
            'required': 'Campo obrigatório, por favor insira o seu endereço de e-mail!',# noqa
        },
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Ex.: jhondoe@email.com'
            }
        )
    )

    password = forms.CharField(
        required=True,
        label='Senha',
        help_text='Digite uma senha de no mínimo 8 caracteres.',
        error_messages={
            'required': 'Campo obrigatório, por favor insira a sua senha!',
        },
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Insira uma senha'
            }
        )
    )

    password_confirmation = forms.CharField(
        required=True,
        label='Confirmação de Senha',
        help_text='Digite novamente a sua senha.',
        error_messages={
            'required': 'Campo obrigatório, por favor insira novamente a sua senha!', # noqa
        },
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repita a senha'
            }
        )
    )

    def clean_username(self):
        dado = self.cleaned_data.get('username')
        exist = User.objects.filter(username=dado).exists()
        if exist:
            raise ValidationError(
                'Nome de usuário já cadastrado, insira um novo',
                code='invalid'
            )
        return dado

    def clean_email(self):
        dado = self.cleaned_data.get('email')
        exist = User.objects.filter(email=dado).exists()
        if exist:
            raise ValidationError(
                'Endereço de e-mail já cadastrado, insira um novo',
                code='invalid'
            )
        return dado

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password')
        password2 = cleaned_data.get('password_confirmation')
        if password1 != password2:
            raise ValidationError({
                'password': ValidationError(
                    'Ambas as senhas devem ser iguais',
                    code='invalid'
                ),
                'password_confirmation': ValidationError(
                    'Ambas as senhas devem ser iguais',
                    code='invalid'
                )
            })

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'password_confirmation'
        ]
