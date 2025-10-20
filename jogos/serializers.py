from rest_framework import serializers
from jogos.models import Jogo
from django.db.models import Avg

class JogoSerializer(serializers.ModelSerializer):

    media_avaliacoes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Jogo
        fields = '__all__'

    def get_media_avaliacoes(self, obj):
        media = obj.reviews.aggregate(Avg('estrelas'))
        
        if media:
            return round(media, 1)  

        return None