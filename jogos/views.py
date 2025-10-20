from rest_framework import generics
from jogos.models import Jogo
from jogos.serializers import JogoSerializer
from rest_framework.permissions import IsAuthenticated
from jogos.permissions import JogoPermission    

class ListCreateJogoView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer

class RetrieveUpdateDestroyJogoView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer