from django import forms


class LoginForm(forms.Form):
    email = forms.CharField(
        required=True,
        label='E-mail',
        help_text='Insira o seu endereço de e-mail já cadastrado',
        error_messages={
            'required': 'Campo obrigatório, por favor insira o seu e-mail'
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
        help_text='Insira a senha da sua conta',
        error_messages={
            'required': 'Campo obrigatório, por favor insira a seu senha'
        },
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Senha da conta'
            }
        )
    )
