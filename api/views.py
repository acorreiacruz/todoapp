from rest_framework import viewsets
from todo.models import Tarefa
from .serializers import TarefaSerializer


class TarefaModelViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    http_method_names = ['get', 'post', 'patch', 'delete', 'options', 'head']
