from django.test import TestCase
from django.urls import resolve, reverse

from .models import Tarefa
from .views import (cadastrar_tarefas, cadastrar_tarefas_validar,
                    detalhar_tarefas, listar_tarefas)


class TarefasTest(TestCase):

    def setUp(self) -> None:
        
        return super().setUp()


    def test_if_listar_tarefas_view_url_esta_correta(self):
        url = reverse("todo:listar")
        self.assertEqual('/',url)


    def test_se_funcao_da_view_listar_tarefas_esta_correta(self):
        url = reverse("todo:listar")
        resolve_object = resolve(url)
        self.assertIs(resolve_object.func, listar_tarefas)


    def test_se_template_da_view_listar_tarefas_esta_correto(self): 
        response = self.client.get(reverse("todo:listar"))
        self.assertTemplateUsed(response,"todo/pages/list.html")


    def test_se_view_listar_tarefas_retornar_status_code_200(self):
        url = reverse("todo:listar")
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)


    def test_se_funcao_da_view_detalhar_tarefas_esta_correta(self):
        resolve_object = resolve(reverse('todo:detalhar', kwargs={'pk':1}))
        self.assertIs(resolve_object.func, detalhar_tarefas)
    
    
    def test_if_detalhar_tarefas_view_template_esta_correta(self):
        response = self.client.get(reverse('todo:detalhar'), kwargs={'pk':1})
        self.assertTemplateUsed(response, 'todo/pages/detail.html')


    def test_se__view_detalhar_tarefas_retorna_status_code_404(self):
        response = self.client.get(reverse("todo:detalhar", kwargs={'pk':1000}))
        self.assertEqual(response.status_code, 404)


    def test_se_url_da_view_cadastrar_tarefas_esta_correta(self):
        url = reverse('todo:cadastrar')
        self.assertEqual('/tarefas/cadastrar/', url)


    def test_se_funcao_da_view_cadastrar_tarefas_esta_correta(self):
        resolve_object = resolve(reverse('todo:cadastrar'))
        self.assertIs(resolve_object.func, cadastrar_tarefas)


    def test_se_template_da_view_cadastrar_tarefas_esta_correto(self):
        response = self.client.get(reverse('todo:cadastrar'))
        self.assertTemplateUsed(response, 'todo/pages/create.html')
    

    def test_se_view_cadastrar_tarefa_retorna_status_code_200(self):
        response = self.client.get(reverse('todo:cadastrar'))
        self.assertEqual(response.status_code, 200)

    
    def test_se_url_da_view_cadastrar_tarefas_validar_esta_correta(self):
        url = reverse('todo:cadastrar_validar')
        self.assertEqual('/tarefas/cadastrar/validar/', url)

    
    def test_se_funcao_da_view_cadastrar_tarefas_validar_esta_correta(self):
        resolve_object = resolve(reverse('todo:cadastrar_validar'))
        self.assertIs(resolve_object.func, cadastrar_tarefas_validar)


    def test_se_view_cadastrar_tarefas_validar_retorna_status_code_404(self):
        response = self.client.get(reverse('todo:cadastrar_validar'), follow=True)
        self.assertEqual(response.status_code, 404)
    
    

