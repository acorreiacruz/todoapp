from django.contrib.auth.models import User
from todo.models import Tarefa


class TestAPIMixin:
    def criar_user(
        self,
        first_name='jhon',
        last_name='doe',
        username='jhondoe',
        email='jhondoe@email.com',
        password='Q@z321654'
    ):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password
        )

    def criar_tarefa(
        self,
        title='Titulo da tarefa sendo criada!',
        description='Descrição da tarefa sendo criada!',
        author=None
    ):
        if author is None:
            author = {}

        return Tarefa.objects.create(
            title=title,
            description=description,
            author=self.criar_user(**author)
        )

    def criar_conjunto_de_tarefas(self, qnt=12):
        tarefas = []
        for i in range(qnt):
            dados_tarefa = {
                'title': f'Título da tarefa {i+1} sendo criada!',
                'description': f'Descrição da tarefa {i+1} sendo criada!'
            }
            tarefa = self.criar_tarefa(**dados_tarefa)
            tarefas.append(tarefa)
        return tarefas
