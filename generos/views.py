from rest_framework import generics
from generos.models import Genero
from generos.serializers import GeneroSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import ViewPermission

class GenerosListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, ViewPermission)
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer


class GenerosRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, ViewPermission)
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
