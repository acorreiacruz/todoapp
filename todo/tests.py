from django.urls import reverse, resolve
from django.test import TestCase
from .views import listar_tarefas


# Create your tests here.
class TarefasTest(TestCase):

    def test_if_listar_tarefas_url_is_correct(self):
        url = reverse("todo:listar_tarefas")
        self.assertEqual('/',url)

    def test_if_listar_tarefas_function_is_corect(self):
        url = reverse("todo:listar_tarefas")
        resolve_object = resolve(url)
        self.assertIs(resolve_object.func, listar_tarefas)

    def test_if_listar_tarefas_template_is_correct(self):
        url = reverse("todo:listar_tarefas")
        resolve_object = resolve(url)
        self.assertEqual(1,2)

    def test_if_listar_tarefas_return_200_status_code(self):
        url = reverse("todo:listar_tarefas")
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)