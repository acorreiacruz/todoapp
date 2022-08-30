# flake8: noqa
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from todo.models import Tarefa
from .serializers import TarefaSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from .pagination import PaginacaoCustomizada
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action


class TarefaModelViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all().filter(done=False)
    serializer_class = TarefaSerializer
    http_method_names = ['get', 'post', 'patch', 'delete', 'options', 'head']
    permission_classes = [IsAuthenticated,]
    pagination_class = [PaginacaoCustomizada,]

    def get_object(self):
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(
            self.get_queryset(),
            pk=pk
        )
        self.check_object_permissions(self.request, obj)
        return obj

    def get_permissions(self):
        if self.request.method in ['GET', 'PATCH', 'DELETE']:
            return [IsOwner(),]

        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'options', 'head']

    def get_queryset(self):
        qs = super().get_queryset().filter(pk=self.request.user.id)
        return qs

    @action(detail=False, url_path='api/me/', url_name='api-usuarios-me')
    def me(self, *args, **kwargs):
        user = self.get_queryset()
        serializer = self.get_serializer(instance=user)
        return Response(serializer.data)
