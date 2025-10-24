from django.db import models

NACIONALIDADE_CHOICES = (
    ('EUA', 'Estados Unidos'),
    ('JPN', 'Japão'),
)


class Diretor(models.Model):
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField(null=True, blank=True)
    nacionalidade = models.CharField(
        max_length=100,
        choices=NACIONALIDADE_CHOICES,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nome
