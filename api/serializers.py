from rest_framework import serializers
from ..todo.models import Tarefa


class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = ['id', 'title', 'description', 'author']