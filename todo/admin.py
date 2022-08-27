from django.contrib import admin
from .models import Tarefa


class TarefaModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'done', 'author')
    list_filter = ['done']
    list_per_page = 10


admin.site.register(Tarefa, TarefaModelAdmin)
