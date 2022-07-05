from django.test import TestCase as DjangoTestCase
from unittest import TestCase
from django.urls import reverse
from parameterized import parameterized
from ..forms import CadastrarForm  # type: ignore


class FormularioCadastrarUnittest(TestCase):

    @parameterized.expand([
        ('first_name', 'Primeiro Nome'),
        ('last_name', 'Último Nome'),
        ('username', 'Nome de Usuário'),
        ('email', 'E-mail'),
        ('password', 'Senha'),
        ('password_confirmation', 'Confirmação de Senha'),
    ])
    def test_se_label_dos_campos_esta_correto(self, field, label):
        form = CadastrarForm()
        self.assertEqual(form[field].field.label, label)

    @parameterized.expand([
        ('first_name', 'Digite o seu primeiro nome, utilizando de 3 a 50 caracteres'),# noqa
        ('last_name', 'Digite o seu último nome, utilizando de 3 a 50 caracteres'),# noqa
        ('username', 'Digite o seu nome de usuário, utilizando de 3 a 50 caracteres'),# noqa
        ('email', 'Insira um endereço de e-mail válido.'),
        ('password', 'Digite uma senha de no mínimo 8 caracteres.'),
        ('password_confirmation', 'Digite novamente a sua senha.'),
    ])
    def test_se_help_text_dos_campos_esta_correto(self, field, help_text):
        form = CadastrarForm()
        self.assertEqual(form[field].field.help_text, help_text)

    @parameterized.expand([
        ('first_name', 'Ex.: Jhon'),
        ('last_name', 'Ex.: Doe'),
        ('username', 'Ex.: jhondoe'),
        ('email', 'Ex.: jhondoe@email.com'),
        ('password', 'Insira uma senha'),
        ('password_confirmation', 'Repita a senha'),
    ])
    def test_se_placeholder_dos_campos_esta_correto(self, field, placeholder):
        form = CadastrarForm()
        self.assertEqual(
            form[field].field.widget.attrs['placeholder'],
            placeholder
        )

    @parameterized.expand([
        ('first_name', 'Campo obrigatório, por favor insira o seu primeiro nome!'),# noqa
        ('last_name', 'Campo obrigatório, por favor insira o seu último nome!'),# noqa
        ('username', 'Campo obrigatório, por favor insira o seu nome de usuário!'),# noqa
        ('email', 'Campo obrigatório, por favor insira o seu endereço de e-mail!'),# noqa
        ('password', 'Campo obrigatório, por favor insira a sua senha!'),
        ('password_confirmation', 'Campo obrigatório, por favor insira novamente a sua senha!'),# noqa
    ])
    def test_se_required_error_message_dos_campos_esta_correta(
        self,
        field,
        required
    ):
        form = CadastrarForm()
        self.assertEqual(
            form[field].field.error_messages['required'],
            required
        )

    @parameterized.expand([
        ('first_name', 'O primeiro nome deve ter no mínimo 3 caracteres'),
        ('last_name', 'O último nome deve ter no mínimo 3 caracteres'),
        ('username', 'O nome de usuário deve ter no mínimo 3 caracteres'),
    ])
    def test_se_min_length_error_message_dos_campos_esta_correta(
        self,
        field,
        required
    ):
        form = CadastrarForm()
        self.assertEqual(
            form[field].field.error_messages['min_length'],
            required
        )

    @parameterized.expand([
        ('first_name', 'O primeiro nome deve ter no máximo 50 caracteres'),
        ('last_name', 'O último nome deve ter no máximo 50 caracteres'),
        ('username', 'O nome de usuário deve ter no máximo 50 caracteres'),
    ])
    def test_se_max_length_error_message_dos_campos_esta_correta(
        self,
        field,
        required
    ):
        form = CadastrarForm()
        self.assertEqual(
            form[field].field.error_messages['max_length'],
            required
        )


class FormularioCadastrarIntegrationTest(DjangoTestCase):

    def setUp(self) -> None:
        self.data = {
            'first_name': 'Jhon',
            'last_name': 'Doe',
            'username': 'jhondoe',
            'email': 'jhondoe@email.com',
            'password': 'Qaz321654',
            'password_confirmation': 'Qaz321654',
        }
        return super().setUp()

    @parameterized.expand([
        'Primeiro Nome',
        'Último Nome',
        'Nome de Usuário',
        'E-mail',
        'Senha',
        'Confirmação de Senha',
    ])
    def test_se_label_dos_campos_e_mostrado_no_template(self, label):
        resposta = self.client.get(
            reverse('usuarios:cadastrar')
        )
        conteudo = resposta.content.decode('utf-8')
        self.assertIn(label, conteudo)

    @parameterized.expand([
        'Digite o seu primeiro nome, utilizando de 3 a 50 caracteres',
        'Digite o seu último nome, utilizando de 3 a 50 caracteres',
        'Digite o seu nome de usuário, utilizando de 3 a 50 caracteres',
        'Insira um endereço de e-mail válido.',
        'Digite uma senha de no mínimo 8 caracteres.',
        'Digite novamente a sua senha.',
    ])
    def test_se_help_text_dos_campos_e_mostrado_no_template(self, help_text):
        resposta = self.client.get(
            reverse('usuarios:cadastrar')
        )
        conteudo = resposta.content.decode('utf-8')
        self.assertIn(help_text, conteudo)

    @parameterized.expand([
        'Ex.: Jhon',
        'Ex.: Doe',
        'Ex.: jhondoe',
        'Ex.: jhondoe@email.com',
        'Insira uma senha',
        'Repita a senha',
    ])
    def test_se_placeholder_dos_campos_e_mostrado_no_template(
        self,
        placeholder
    ):
        resposta = self.client.get(
            reverse('usuarios:cadastrar')
        )
        conteudo = resposta.content.decode('utf-8')
        self.assertIn(placeholder, conteudo)

    @parameterized.expand([
        ('first_name', 'Campo obrigatório, por favor insira o seu primeiro nome!'),# noqa
        ('last_name', 'Campo obrigatório, por favor insira o seu último nome!'),# noqa
        ('username', 'Campo obrigatório, por favor insira o seu nome de usuário!'),# noqa
        ('email', 'Campo obrigatório, por favor insira o seu endereço de e-mail!'),# noqa
        ('password', 'Campo obrigatório, por favor insira a sua senha!'),
        ('password_confirmation', 'Campo obrigatório, por favor insira novamente a sua senha!'),# noqa
    ])
    def test_se_required_error_e_mostrado_no_template(self, field, error):
        self.data[field] = ''
        resposta = self.client.post(
            reverse('usuarios:cadastrar_validar'),
            self.data,
            follow=True
        )
        conteudo = resposta.content.decode('utf-8')
        self.assertIn(error, conteudo)

    @parameterized.expand([
        ('first_name', 'O primeiro nome deve ter no mínimo 3 caracteres', 3),
        ('last_name', 'O último nome deve ter no mínimo 3 caracteres', 3),
        ('username', 'O nome de usuário deve ter no mínimo 3 caracteres', 3),
    ])
    def test_se_min_length_error_e_mostrado_no_template(
        self,
        field,
        error,
        min
    ):
        self.data[field] = 'A' * (min - 1)
        resposta = self.client.post(
            reverse('usuarios:cadastrar_validar'),
            self.data,
            follow=True
        )
        conteudo = resposta.content.decode('utf-8')
        self.assertIn(error, conteudo)

    @parameterized.expand([
        ('first_name', 'O primeiro nome deve ter no máximo 50 caracteres', 50),
        ('last_name', 'O último nome deve ter no máximo 50 caracteres', 50),
        ('username', 'O nome de usuário deve ter no máximo 50 caracteres', 50),
    ])
    def test_se_max_length_error_e_mostrado_no_template(
        self,
        field,
        error,
        max
    ):
        self.data[field] = 'A' * (max + 1)
        resposta = self.client.post(
            reverse('usuarios:cadastrar_validar'),
            self.data,
            follow=True
        )
        conteudo = resposta.content.decode('utf-8')
        self.assertIn(error, conteudo)

    def test_se_error_de_nome_de_usuario_ja_cadastrado_e_mostrado_no_template(
        self
    ):
        url = reverse('usuarios:cadastrar_validar')
        self.client.post(
            url,
            self.data,
            follow=True
        )

        self.data['email'] = 'jhondoe2@email.com'
        resposta = self.client.post(
            url,
            self.data,
            follow=True
        )

        conteudo = resposta.content.decode('utf-8')
        msg = 'Nome de usuário já cadastrado, insira um novo'
        self.assertIn(msg, conteudo)

    def test_se_error_de_email_ja_cadastrado_e_mostrado_no_template(self):
        url = reverse('usuarios:cadastrar_validar')
        self.client.post(
            url,
            self.data,
            follow=True
        )

        self.data['username'] = 'jhondoe2'
        resposta = self.client.post(
            url,
            self.data,
            follow=True
        )

        conteudo = resposta.content.decode('utf-8')
        msg = 'Endereço de e-mail já cadastrado, insira um novo'
        self.assertIn(msg, conteudo)

    def test_de_erro_de_password_e_password_confirmation_diferentes(self):
        url = reverse('usuarios:cadastrar_validar')
        self.data['password'] = 'P@ssword1'
        resposta = self.client.post(url, self.data, follow=True)

        conteudo = resposta.content.decode('utf-8')
        msg = 'Ambas as senhas devem ser iguais'
        self.assertIn(msg, conteudo)

    def teste_login_de_usuario_cadastrado(self):
        self.client.post(
            reverse('usuarios:cadastrar_validar'),
            self.data,
            follow=True
        )

        usuario_autenticado = self.client.login(
            username='jhondoe',
            password='Qaz321654',
        )

        self.assertTrue(usuario_autenticado)
