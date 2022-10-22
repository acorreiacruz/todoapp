from django.contrib import admin
from .models import Tarefa


class TarefaModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'done', 'author')
    list_editable = 'done', 'title'
    list_filter = ['done', 'author']
    list_per_page = 10


admin.site.register(Tarefa, TarefaModelAdmin)
