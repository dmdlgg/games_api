from rest_framework import serializers
from generos.serializers import GeneroSerializer
from diretores.serializers import DiretorSerializer
from desenvolvedora.serializers import DesenvolvedoraSerializer
from jogos.models import Jogo
from django.db.models import Avg


# retorno para requisições POST
class JogoSerializer(serializers.ModelSerializer):

    media_avaliacoes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Jogo
        fields = '__all__'

    def get_media_avaliacoes(self, obj):
        media = obj.reviews.aggregate(Avg('estrelas'))['estrelas__avg']

        if media:
            return round(media, 1)

        return None


# retorno para requisições GET
class JogoDetailSerializer(serializers.ModelSerializer):

    genero = GeneroSerializer(many=True)
    diretor = DiretorSerializer(many=True)
    desenvolvedora = DesenvolvedoraSerializer(many=True)

    class Meta:
        model = Jogo
        fields = ['nome', 'diretor', 'genero', 'desenvolvedora', 'data_lancamento', 'sinopse', 'media_avaliacoes']

    media_avaliacoes = serializers.SerializerMethodField(read_only=True)

    def get_media_avaliacoes(self, obj):
        media = obj.reviews.aggregate(Avg('estrelas'))['estrelas__avg']

        if media:
            return round(media, 1)

        return None
