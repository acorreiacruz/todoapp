from django.db import models
from django.contrib.auth.models import User


class Tarefa(models.Model):

    title = models.CharField(max_length=150, null=False, blank=False)
    description = models.CharField(max_length=300, null=False, blank=False)
    done = models.BooleanField(null=True, default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
