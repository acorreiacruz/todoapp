from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

app_name = 'api'

api_todo_urls = SimpleRouter()
api_todo_urls.register(
    prefix='tarefas',
    viewset=views.TarefaModelViewSet,
    basename='todo-api'
)

print(api_todo_urls.urls)

urlpatterns = [
    path('', include(api_todo_urls.urls)),
]
