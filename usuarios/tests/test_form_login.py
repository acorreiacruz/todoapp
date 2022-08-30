from django.test import TestCase
from parameterized import parameterized
from ..forms import LoginForm  # type: ignore
from django.urls import reverse
from django.contrib.auth.models import User


class LoginFormTest(TestCase):

    def criar_usuario(
        self,
        first_name="jhon",
        last_name='doe',
        username='jhondoe',
        email='jhondoe@email.com',
        password='Q@z321654'
    ):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password
        )

    @parameterized.expand([
        ('username', 'Nome de Usuário'),
        ('password', 'Senha')
    ])
    def teste_se_label_dos_campos_esta_correto(self, field, label):
        form = LoginForm()
        self.assertEqual(form[field].field.label, label)
        resposta = self.client.get(
            reverse('usuarios:login')
        )
        conteudo = resposta.content.decode('utf-8')
        self.assertIn(label, conteudo)

    @parameterized.expand([
        ('username', 'Ex.: jhondoe'),
        ('password', 'Senha da conta')
    ])
    def teste_se_placeholder_dos_campos_esta_correto(self, field, placeholder):
        form = LoginForm()
        self.assertEqual(
            form[field].field.widget.attrs['placeholder'],
            placeholder
        )
        resposta = self.client.get(
            reverse('usuarios:login')
        )
        conteudo = resposta.content.decode('utf-8')
        self.assertIn(placeholder, conteudo)

    @parameterized.expand([
        ('username', 'Insira o seu endereço de e-mail já cadastrado'),
        ('password', 'Insira a senha da sua conta')
    ])
    def teste_se_help_text_dos_campos_esta_correto(self, field, help_text):
        form = LoginForm()
        self.assertEqual(
            form[field].field.help_text,
            help_text
        )
        # resposta = self.client.get(
        #     reverse('usuarios:login')
        # )
        # conteudo = resposta.content.decode('utf-8')
        # self.assertIn(help_text, conteudo)

    def test_de_login(self):
        user = self.criar_usuario()
        resposta = self.client.login(
            username=user.username,
            password=user.password
        )
        self.assertTrue(resposta)
