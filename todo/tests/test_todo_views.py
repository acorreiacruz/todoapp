from .tarefa_test_base import TarefaTestBase
from django.urls import resolve, reverse
from ..models import Tarefa  # type: ignore
from ..views import (  # type: ignore
        buscar_tarefas,
        cadastrar_tarefas,
        cadastrar_tarefas_validar,
        detalhar_tarefas,
        excluir_tarefa,
        finalizar_tarefa,
        listar_tarefas
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
