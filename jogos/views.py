from rest_framework import generics, views, response, status 
from jogos.models import Jogo
from jogos.serializers import JogoSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import ViewPermission

class ListCreateJogoView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, ViewPermission)
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer

class RetrieveUpdateDestroyJogoView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, ViewPermission)
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer

class JogosStatsView(views.APIView):
    permission_classes = (IsAuthenticated, ViewPermission)

    def get(self, request):
        return response.Response(
            data= {
                "message": "funcionou"
            },
            status=status.HTTP_200_OK
        )