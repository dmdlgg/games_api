from rest_framework import serializers
from desenvolvedora.models import Desenvolvedora


class DesenvolvedoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desenvolvedora
        fields = ['id', 'nome']
