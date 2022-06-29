from django.test import TestCase
from ..models import Tarefa  # type: ignore


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
