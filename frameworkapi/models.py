from django.db import models

class JsonPlaceholder(models.Model):
    """Classe responsavel pela criaçao dos dados a serem retornados em JSON """
    userId = models.CharField(max_length=50)
    id = models.CharField(primary_key=True, max_length=2)
    title = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title.title()