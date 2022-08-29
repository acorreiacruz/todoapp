from rest_framework import viewsets
from todo.models import Tarefa
from .serializers import TarefaSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner


class TarefaModelViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    http_method_names = ['get', 'post', 'patch', 'delete', 'options', 'head']
    permission_classes = [IsAuthenticated]
