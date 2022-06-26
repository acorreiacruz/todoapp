from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import resolve, reverse
from parameterized import parameterized
from .forms import Cadastrar
from .models import Tarefa
from .views import (
        buscar_tarefas,
        cadastrar_tarefas,
        cadastrar_tarefas_validar,
        detalhar_tarefas,
        excluir_tarefa,
        finalizar_tarefa,
        listar_tarefas
    )


class TarefaTestBase(TestCase):

    def criar_tarefa(
        self,
        title='Título da Tarefa',
        description='Descrição da Tarefa',
    ):

        return Tarefa.objects.create(
            title=title,
            description=description,
        )


class TarefasTest(TarefaTestBase):

    def test_se_url_da_view_listar_tarefas_esta_correta(self):
        url = reverse("todo:listar")
        self.assertEqual('/', url)

    def test_se_funcao_da_view_listar_tarefas_esta_correta(self):
        url = reverse("todo:listar")
        resolve_object = resolve(url)
        self.assertIs(resolve_object.func, listar_tarefas)

    def test_se_template_da_view_listar_tarefas_esta_correto(self):
        response = self.client.get(reverse("todo:listar"))
        self.assertTemplateUsed(response, "todo/pages/list.html")

    def test_se_view_listar_tarefas_retorna_status_code_200(self):
        url = reverse("todo:listar")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_se_view_listar_tarefas_retorna_msgm_de_tarefas_finalizadas(self):
        resposta = self.client.get(
            reverse('todo:listar')
        )
        msg = 'Todas as tarefas foram atualizadas!'
        conteudo_resposta = resposta.content.decode('utf-8')
        self.assertIn(msg, conteudo_resposta)

    def test_se_context_da_view_listar_tarefas_esta_correto(self):
        tarefa = self.criar_tarefa()
        resposta = self.client.get(
            reverse('todo:listar')
        )
        resposta_context = resposta.context['tarefas'].first()

        self.assertEqual(resposta_context.title, tarefa.title)
        self.assertEqual(resposta_context.description, tarefa.description)
        self.assertEqual(resposta_context.done, tarefa.done)
        self.assertEqual(resposta_context.id, tarefa.id)

    def test_se_template_da_view_listar_tarefas_carrega_tarefa(self):
        tarefa = self.criar_tarefa()
        resposta = self.client.get(reverse('todo:listar'))
        conteudo = resposta.content.decode('utf-8')
        self.assertIn(tarefa.title, conteudo)

    def test_se_view_listar_tarefas_nao_retorna_tarefa_feita(self):
        tarefa = self.criar_tarefa()
        Tarefa.objects.filter(id=tarefa.id).update(done=True)
        resposta = self.client.get(
            reverse('todo:listar')
        )
        resposta_context = resposta.context['tarefas'].first()
        self.assertEqual(resposta_context, None)

    def test_se_template_da_view_listar_tarefas_nao_carrega_tarefa_feita(self):
        tarefa = self.criar_tarefa()
        Tarefa.objects.filter(id=tarefa.id).update(done=True)
        resposta = self.client.get(
            reverse('todo:listar')
        )
        resposta_content = resposta.content.decode('utf-8')
        self.assertNotIn(tarefa.title, resposta_content)

    def test_se_url_da_view_detalhar_tarefas_esta_correta(self):
        url = reverse('todo:detalhar', kwargs={'pk': 1})
        self.assertEqual('/tarefas/detalhar/1/', url)

    def test_se_funcao_da_view_detalhar_tarefas_esta_correta(self):
        resolve_object = resolve(reverse('todo:detalhar', kwargs={'pk': 1}))
        self.assertIs(resolve_object.func, detalhar_tarefas)

    def test_se_template_da_view_detalhar_tarefas_esta_correto(self):
        self.criar_tarefa()
        response = self.client.get(reverse('todo:detalhar', kwargs={'pk': 1}))
        self.assertTemplateUsed(response, 'todo/pages/detail.html')

    def test_se_view_detalhar_tarefas_retorna_status_code_404(self):
        response = self.client.get(
            reverse("todo:detalhar", kwargs={'pk': 100})
        )
        self.assertEqual(response.status_code, 404)

    def test_se_view_detalhar_tarefas_retorna_status_code_200(self):
        self.criar_tarefa()
        resposta = self.client.get(
            reverse('todo:detalhar', kwargs={'pk': 1})
        )
        self.assertEqual(resposta.status_code, 200)

    def teste_se_o_context_da_view_detalhar_tarefas_esta_correto(self):
        tarefa = self.criar_tarefa()
        resposta = self.client.get(
            reverse('todo:detalhar', kwargs={'pk': 1})
        )
        resposta_context = resposta.context['tarefa']
        self.assertEqual(tarefa.title, resposta_context.title)
        self.assertEqual(tarefa.description, resposta_context.description)

    def teste_se_template_da_view_detalhar_tarefas_detalha_a_tarefa(self):
        tarefa = self.criar_tarefa()
        resposta = self.client.get(
            reverse('todo:detalhar', kwargs={'pk': 1})
        )
        conteudo = resposta.content.decode('utf-8')
        self.assertIn(tarefa.title, conteudo)
        self.assertIn(tarefa.description, conteudo)

    def test_se_url_da_view_cadastrar_tarefas_esta_correta(self):
        url = reverse('todo:cadastrar')
        self.assertEqual('/tarefas/cadastrar/', url)

    def test_se_funcao_da_view_cadastrar_tarefas_esta_correta(self):
        resolve_object = resolve(reverse('todo:cadastrar'))
        self.assertIs(resolve_object.func, cadastrar_tarefas)

    def test_se_template_da_view_cadastrar_tarefas_esta_correto(self):
        response = self.client.get(reverse('todo:cadastrar'))
        self.assertTemplateUsed(response, 'todo/pages/create.html')

    def test_se_view_cadastrar_tarefas_retorna_status_code_200(self):
        response = self.client.get(reverse('todo:cadastrar'))
        self.assertEqual(response.status_code, 200)

    def test_se_url_da_view_cadastrar_tarefas_validar_esta_correta(self):
        url = reverse('todo:cadastrar_validar')
        self.assertEqual('/tarefas/cadastrar/validar/', url)

    def test_se_funcao_da_view_cadastrar_tarefas_validar_esta_correta(self):
        resolve_object = resolve(reverse('todo:cadastrar_validar'))
        self.assertIs(resolve_object.func, cadastrar_tarefas_validar)

    def test_se_get_para_view_cadastrar_tarefas_validar_retorna_code_404(
        self
    ):
        resposta = self.client.get(reverse("todo:cadastrar_validar"))
        self.assertEqual(resposta.status_code, 404)

    def test_se_url_da_view_excluir_tarefas_esta_correta(self):
        url = reverse('todo:finalizar', kwargs={'pk': 1})
        self.assertEqual('/tarefas/finalizar/1/', url)

    def test_se_funcao_da_view_excluir_tarefas_esta_correta(self):
        objeto_resolve = resolve(reverse('todo:excluir', kwargs={'pk': 1}))
        self.assertIs(excluir_tarefa, objeto_resolve.func)

    def teste_se_view_exluir_tarefas_exclui_a_tarefa(self):
        tarefa = self.criar_tarefa()
        resposta = self.client.get(reverse('todo:excluir', kwargs={'pk': 1}))
        conteudo = resposta.content.decode('utf-8')
        self.assertNotIn(tarefa.title, conteudo)

    def test_se_url_da_view_finalizar_tarefas_esta_correta(self):
        url = reverse('todo:finalizar', kwargs={'pk': 1})
        self.assertEqual('/tarefas/finalizar/1/', url)

    def test_se_funcao_da_view_finalizar_tarefa_esta_correta(self):
        objeto_resolve = resolve(reverse('todo:finalizar', kwargs={'pk': 1}))
        self.assertIs(finalizar_tarefa, objeto_resolve.func)

    def teste_se_view_finalizar_tarefas_finaliza_a_tarefa(self):
        tarefa = self.criar_tarefa()
        resposta = self.client.get(reverse('todo:finalizar', kwargs={'pk': 1}))
        conteudo = resposta.content.decode('utf-8')
        self.assertNotIn(tarefa.title, conteudo)

    def test_url_da_view_buscar_tarefas(self):
        url = reverse('todo:buscar')
        self.assertEqual('/tarefas/buscar/', url)

    def test_do_template_da_view_buscar_tarefas(self):
        resposta = self.client.get(reverse('todo:buscar'))
        self.assertTemplateUsed(resposta, 'todo/pages/list.html')

    def test_da_funcao_da_view_buscar_tarefas(self):
        objeto_resolve = resolve(reverse('todo:buscar'))
        self.assertIs(buscar_tarefas, objeto_resolve.func)

    def test_se_view_buscar_tarefas_retorna_status_code_200(self):
        resposta = self.client.get(reverse('todo:buscar'))
        self.assertEqual(resposta.status_code, 200)

    def test_se_view_buscar_tarefas_retorna_tarefa_correta(self):
        tarefa = self.criar_tarefa(title='Tarefa Buscada')
        resposta = self.client.get(
            reverse('todo:buscar'),
            {'q': 'Tarefa Buscada'}
        )
        self.assertIn(tarefa.title, resposta.content.decode('utf-8'))

    def test_se_view_buscar_tarefas_nao_retorna_tarefa_correta(self):
        tarefa = self.criar_tarefa(title='Tarefa Buscada')
        resposta = self.client.get(
            reverse('todo:buscar'),
            {'q': 'Z'}
        )
        self.assertNotIn(tarefa.title, resposta.content.decode('utf-8'))


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


class TestModelTarefa(TarefaTestBase):

    def setUp(self) -> None:
        self.tarefa = self.criar_tarefa()
        return super().setUp()

    @parameterized.expand([
        ('title', 150),
        ('description', 300)
    ])
    def teste_se_campo_levanta_erro_de_comprimento_maximo(
        self,
        campo,
        max_length
    ):
        setattr(self.tarefa, campo, 'A'*(max_length + 1))
        with self.assertRaises(ValidationError):
            self.tarefa.full_clean()

    def test_se_campo_done_da_tarefa_e_falso_por_padrao(self):
        tarefa = self.criar_tarefa()
        self.assertFalse(tarefa.done)

    def test_se_string_representando_a_tarefa_e_o_titulo(self):
        self.assertEqual(
            str(self.tarefa),
            self.tarefa.title
        )
