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
    path(
        'login/',
        views.login_view,
        name='login'
    ),
    path(
        'login/validar/',
        views.login_view_validar,
        name='login_validar'
    ),
    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),
]
