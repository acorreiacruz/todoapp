from rest_framework import viewsets
from ..todo.models import Tarefa


class TarefaModelViewSet(viewsets.ModelViewSet):
    queryset = Tarefa
    http_method_names = ['get', 'post', 'patch', 'delete', 'options', 'head']
