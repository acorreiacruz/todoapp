from django.urls import path

app_name = 'api'

urlpatterns = [
    path('recursos/',lambda n: 2 * n, name='teste' ),
]
