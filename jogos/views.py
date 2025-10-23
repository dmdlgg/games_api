from django.db.models import Count 
from reviews.models import Review
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
    queryset = Jogo.objects.all()

    def get(self, request):
        total_jogos = self.queryset.count()
        jogos_por_genero = self.queryset.values('genero__nome').annotate(count=Count('id'))
        total_reviews = Review.objects.count()


        return response.Response(
            data= {
                "total_jogos": total_jogos,
                "jogos_por_generos": jogos_por_genero,
                "tota_reviews": total_reviews
            },
            status=status.HTTP_200_OK
        )