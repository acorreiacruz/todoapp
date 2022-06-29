from .tarefa_test_base import TarefaTestBase
from django.core.exceptions import ValidationError
from parameterized import parameterized


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
