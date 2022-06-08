from django.db import models


class Tarefa(models.Model):

    title = models.CharField(max_length=120, null=False, blank=False)
    description = models.CharField(max_length=300, null=False, blank=False)
    done = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
