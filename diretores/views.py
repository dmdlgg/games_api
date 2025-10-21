from rest_framework import generics
from diretores.models import Diretor
from diretores.serializers import DiretorSerializer
from rest_framework.permissions import IsAuthenticated
from diretores.permissions import DiretoresPermission

class ListCreateDiretorView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, DiretoresPermission)
    queryset = Diretor.objects.all()
    serializer_class = DiretorSerializer

class RetrieveUpdateDestroyDiretorView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, DiretoresPermission)
    queryset = Diretor.objects.all()
    serializer_class = DiretorSerializer


