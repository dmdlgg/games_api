from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from jogos.models import Jogo


class Review(models.Model):
    jogo = models.ForeignKey(Jogo, on_delete=models.PROTECT, related_name='reviews')
    estrelas = models.IntegerField(
        validators=[
            MinValueValidator(0, 'A avaliação não pode ser inferior a 0 estrelas'),
            MaxValueValidator(5, 'A avaliação não pode ser inferior a 0 estrelas')
        ]
    )
    analise = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.jogo
