from rest_framework import generics
from diretores.models import Diretor
from diretores.serializers import DiretorSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import ViewPermission


class ListCreateDiretorView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, ViewPermission)
    queryset = Diretor.objects.all()
    serializer_class = DiretorSerializer


class RetrieveUpdateDestroyDiretorView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, ViewPermission)
    queryset = Diretor.objects.all()
    serializer_class = DiretorSerializer
