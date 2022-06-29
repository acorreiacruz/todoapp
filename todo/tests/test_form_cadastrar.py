from django.test import TestCase
from parameterized import parameterized
from django.urls import reverse
from ..forms import Cadastrar  # type: ignore


class TestFormularioCadastrar(TestCase):
    def setUp(self) -> None:
        self.data = {
            'title': 'Título da Tarefa',
            'description': 'Descrição da tarefa'
        }
        return super().setUp()

    @parameterized.expand([
        ('title', 'Título da Tarefa'),
        ('description', 'Descrição da Tarefa')
    ])
    def test_se_label_dos_campos_esta_correto_e_se_e_carregado(
        self,
        field,
        label
    ):
        form = Cadastrar(self.data)
        self.assertEqual(form[field].field.label, label)

        resposta = self.client.post(
            reverse('todo:cadastrar_validar'),
            self.data,
            follow=True
        )
        self.assertIn(label, resposta.content.decode('utf-8'))

    @parameterized.expand([
        ('title', 'Ex.: Minha Tarefa'),
        ('description', 'Ex.: Descrição detalhada da tarefa ...')
    ])
    def test_se_placeholder_dos_campos_esta_correto_e_se_e_carregado(
        self,
        field,
        placeholder
    ):
        form = Cadastrar(self.data)
        self.assertEqual(
            form[field].field.widget.attrs['placeholder'],
            placeholder
        )

        resposta = self.client.post(
            reverse('todo:cadastrar_validar'),
            self.data,
            follow=True
        )
        self.assertIn(placeholder, resposta.content.decode('utf-8'))

    @parameterized.expand([
        ('title', 'Insira o título para a sua tarefa, de 4 a 150 caracteres.'),
        (
            'description',
            'Insira a descrição para a tarefa de 4 a 300 caracteres.'
        )
    ])
    def test_se_help_text_dos_campos_esta_correto_e_se_e_carregado(
        self,
        field,
        help_text
    ):
        form = Cadastrar(self.data)
        self.assertEqual(form[field].field.help_text, help_text)

        resposta = self.client.post(
            reverse('todo:cadastrar_validar'),
            self.data,
            follow=True
        )
        self.assertIn(help_text, resposta.content.decode('utf-8'))

    @parameterized.expand([
        ('title', 'Campo obrigatório, por favor insira um título para\
            a tarefa'),
        ('description', 'Campo obrigatório, por favor insira uma descrição para\
            a tarefa')
    ])
    def test_se_mensagem_de_required_esta_correta_e_se_e_carregada(
        self,
        field,
        required
    ):
        self.data[field] = ''
        form = Cadastrar(self.data)
        self.assertIn(required, form.errors.get(field))

        resposta = self.client.post(
            reverse('todo:cadastrar_validar'),
            self.data,
            follow=True
        )
        self.assertIn(required, resposta.content.decode('utf-8'))

    @parameterized.expand([
        ('title', 'O título deve ter no mínimo 4 caracteres', 4),
        ('description', 'A descrição deve ter no mínimo 4 caracteres', 4)
    ])
    def test_se_mensagem_de_min_length_esta_correta_e_se_e_carregada(
        self,
        field,
        msg,
        min
    ):
        self.data[field] = 'A' * (min - 1)
        form = Cadastrar(self.data)
        self.assertIn(msg, form.errors.get(field))

        resposta = self.client.post(
            reverse('todo:cadastrar_validar'),
            self.data,
            follow=True
        )
        self.assertIn(msg, resposta.content.decode('utf-8'))

    @parameterized.expand([
        ('title', 'O título pode ter no máximo 150 caracteres', 150),
        ('description', 'A descrição pode ter no máximo 300 caracteres', 300)
    ])
    def test_se_mensagem_de_max_length_esta_correta_e_se_e_carregada(
        self,
        field,
        msg,
        max
    ):
        self.data[field] = 'A' * (max + 1)
        form = Cadastrar(self.data)
        self.assertIn(msg, form.errors.get(field))

        resposta = self.client.post(
            reverse('todo:cadastrar_validar'),
            self.data,
            follow=True
        )
        self.assertIn(msg, resposta.content.decode('utf-8'))
