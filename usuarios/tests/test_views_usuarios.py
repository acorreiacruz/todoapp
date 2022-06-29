from django.test import TestCase
from django.urls import resolve, reverse
from ..views import (  # type: ignore
    cadastrar,
    cadastrar_validar,
    login_view,
    login_view_validar
    )


class TestUsuariosViews(TestCase):

    def test_se_url_da_view_cadastrar_esta_correta(self):
        url = reverse('usuarios:cadastrar')
        self.assertEqual('/usuarios/cadastrar/', url)

    def test_func_da_view_cadastrar_esta_correta(self):
        objeto_resolve = resolve(reverse('usuarios:cadastrar'))
        self.assertIs(cadastrar, objeto_resolve.func)

    def test_se_template_da_view_cadastrar_esta_correto(self):
        resposta = self.client.get(reverse('usuarios:cadastrar'))
        self.assertTemplateUsed(resposta, 'usuarios/pages/cadastrar.html')

    def test_se_url_da_view_cadastrar_validar_esta_correta(self):
        url = reverse('usuarios:cadastrar_validar')
        self.assertEqual('/usuarios/cadastrar/validar/', url)

    def test_se_funcao_da_view_cadastrar_validar_esta_correta(self):
        objeto_resolve = resolve(reverse('usuarios:cadastrar_validar'))
        self.assertIs(cadastrar_validar, objeto_resolve.func)

    def test_se_view_cadastrar_validar_levanta_erro_404_se_nao_for_post(self):
        resposta = self.client.get(reverse('usuarios:cadastrar_validar'))
        self.assertEqual(resposta.status_code, 404)

    def test_se_url_da_view_login_view_esta_correta(self):
        url = reverse('usuarios:login')
        self.assertEqual(url, '/usuarios/login/')

    def test_se_template_da_view_login_view_esta_correto(self):
        url = reverse('usuarios:login')
        resposta = self.client.get(url)
        self.assertTemplateUsed(resposta, 'usuarios/pages/login.html')

    def test_se_funcao_da_view_login_view_esta_correta(self):
        url = reverse('usuarios:login')
        objeto_resolve = resolve(url)
        self.assertIs(login_view, objeto_resolve.func)

    def test_se_url_da_view_login_view_validar_esta_correta(self):
        url = reverse('usuarios:login_validar')
        self.assertEqual(url, '/usuarios/login/validar/')

    def test_se_funcao_da_view_login_view_validar_esta_correta(self):
        url = reverse('usuarios:login_validar')
        objeto_resolve = resolve(url)
        self.assertIs(login_view_validar, objeto_resolve.func)
