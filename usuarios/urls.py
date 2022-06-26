from django.urls import path
from . import views

app_name = 'usuarios'
urlpatterns = [
    path(
        'cadastrar/',
        views.cadastrar,
        name='cadastrar'
    ),
    path(
        'cadastrar/validar/',
        views.cadastrar_validar,
        name='cadastrar_validar'
    ),
]
