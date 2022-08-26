from django.contrib import admin
from .models import Tarefa


class TarefaModelAdmin(admin.ModelAdmin):
    list_fields = ('id', 'titulo', 'feito', 'user')


admin.site.register(Tarefa, TarefaModelAdmin)
