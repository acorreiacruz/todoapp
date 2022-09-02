from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


app_name = 'api'

api_tarefas_urls = SimpleRouter()
api_tarefas_urls.register(
    prefix='tarefas',
    viewset=views.TarefaModelViewSet,
    basename='todo-api-tarefas'
)

api_users_urls = SimpleRouter()
api_users_urls.register(
    prefix='usuarios',
    viewset=views.UserReadOnlyModelViewSet,
    basename='todo-api-users'
)

print(api_users_urls.urls)
print(api_tarefas_urls.urls)

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
    path('', include(api_tarefas_urls.urls)),
    path('', include(api_users_urls.urls)),
]
