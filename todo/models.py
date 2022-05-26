from django.db import models

class Tarefa(models.Model):

    title = models.CharField(max_length=200, null=False, blank=False)
    done = models.BooleanField()
    description = models.TextField(null= False, blank= False, default="Descricao")

    def __str__(self) -> str:
        return self.title

