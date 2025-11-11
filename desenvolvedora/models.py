from django.db import models


class Desenvolvedora(models.Model):
    nome = models.CharField(max_length=500)

    def __str__(self):
        return self.nome
