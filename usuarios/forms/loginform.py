from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='E-mail',
        help_text='Insira o seu endereço de e-mail já cadastrado',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ex.: jhondoe'
            }
        )
    )

    password = forms.CharField(
        required=True,
        label='Senha',
        help_text='Insira a senha da sua conta',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Senha da conta'
            }
        )
    )
