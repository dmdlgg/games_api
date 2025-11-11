from django.db import models
from generos.models import Genero
from diretores.models import Diretor
from desenvolvedora.models import Desenvolvedora


class Jogo(models.Model):
    nome = models.CharField(max_length=500)
    genero = models.ManyToManyField(Genero, related_name='jogos')
    data_lancamento = models.DateField(null=True, blank=True)
    diretor = models.ManyToManyField(Diretor, related_name='jogos')
    desenvolvedora = models.ManyToManyField(Desenvolvedora, related_name='jogos')
    sinopse = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome
