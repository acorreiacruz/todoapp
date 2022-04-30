from django.db import models

class Tarefa(models.Model):

    titulo = models.CharField(max_length=200, null=False, blank=False)
    feito = models.BooleanField()

    def __str__(self) -> str:
        return f"Tarefa {self.id}"

