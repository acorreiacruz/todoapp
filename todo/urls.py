from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.listar_tarefas, name='listar'),
    path(
        'tarefas/detalhar/<int:pk>/',
        views.detalhar_tarefas,
        name="detalhar"
    ),
    path('tarefas/excluir/<int:pk>/', views.excluir_tarefa, name='excluir'),
    path('tarefas/editar/<int:pk>/', views.editar_tarefas, name="editar"),
    path(
        'tarefas/finalizar/<int:pk>/',
        views.finalizar_tarefa,
        name="finalizar"
    ),
    path('tarefas/cadastrar/', views.cadastrar_tarefas, name='cadastrar'),
    path(
        'tarefas/cadastrar/validar/',
        views.cadastrar_tarefas_validar,
        name='cadastrar_validar'
    ),
    path('tarefas/buscar/', views.buscar_tarefas, name='buscar'),
]
