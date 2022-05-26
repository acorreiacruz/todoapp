from django.db import models

class Tarefa(models.Model):

    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null= False, blank= False, default="Descricao")
    done = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title

