from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


app_name = 'api'

api_todo_urls = SimpleRouter()
api_todo_urls.register(
    prefix='tarefas',
    viewset=views.TarefaModelViewSet,
    basename='todo-api'
)


urlpatterns = [
    path(
        'token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        'token/verify/',
        TokenVerifyView.as_view(),
        name='token_verify'
    ),
    path('', include(api_todo_urls.urls)),
]
