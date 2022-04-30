from django.contrib import admin
from .models import Tarefa

class TarefaModelAdmin(admin.ModelAdmin):
    list_fields = ('titulo','feito')
    
admin.site.register(Tarefa, TarefaModelAdmin)
