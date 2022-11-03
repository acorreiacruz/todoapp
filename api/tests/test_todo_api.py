from rest_framework.test import APITestCase
from .test_api_mixin import TestAPIMixin
from django.urls import reverse


class TestTodoAPI(APITestCase, TestAPIMixin):

    def get_api_url(
        self,
        action='list',
        **kwargs
    ):
        url = reverse(f'api:api-sobreviventes-{action}', kwargs={**kwargs})
        return url

    def get_resposta(
        self,
        action='list',
        method='get',
        content_type='',
        data=None,
        **kwargs
    ):
        if method == 'get':
            resposta = self.client.get(
                self.get_api_url(action=action, **kwargs),
            )

        if method == 'post':
            resposta = self.client.post(
                self.get_api_url(action=action, **kwargs),
                data=data,
                content_type=content_type
            )

        if method == 'delete':
            resposta = self.client.delete(
                self.get_api_url(action=action, **kwargs)
            )

        if method == 'patch':
            resposta = self.client.patch(
                self.get_api_url(action=action, **kwargs),
                data=data
            )
        return resposta

    def test_se_api_retorna_status_code_200_ao_listar(self):
        ...

    def test_se_api_retorna_denied_quando_usuario_nao_autenticado_ao_listar(
        self
    ):
        ...

    def test_se_api_retorna_numero_correto_de_tarefas_ao_listar(self):
        ...

    def test_se_api_retorna_status_code_200_ao_detalhar(self):
        ...

    def test_se_api_retorna_status_code_404_ao_detalhar(self):
        ...

    def test_se_api_detalha_a_tarefa_correta_ao_detalhar(self):
        ...

    def test_se_api_retorna_denied_quando_usuario_nao_autenticado_ao_detalhar(
        self
    ):
        ...

    def test_se_api_retorna_msg_de_unauthorized_ao_detalhar(self):
        ...

    def test_se_api_retorna_status_code_201_ao_criar(self):
        ...

    def test_se_api_cria_tarefa(self):
        ...

    def test_se_api_retorna_denied_quando_usuario_nao_autenticado_ao_criar(
        self
    ):
        ...

    def test_se_api_retorna_status_code_202_ao_deletar(self):
        ...

    def test_se_api_retorna_status_code_401_ao_deletar(self):
        ...

    def test_se_api_nao_permite_deletar_tarefa_nao_autenticado(self):
        ...

    def test_se_api_nao_permite_excluir_tarefa_de_outro_usuario(self):
        ...

