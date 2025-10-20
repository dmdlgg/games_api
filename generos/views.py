from rest_framework import generics
from generos.models import Genero
from generos.serializers import GeneroSerializer
from rest_framework.permissions import IsAuthenticated
from generos.permissions import GeneroPermission

class GenerosListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GeneroPermission)
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer


class GenerosRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GeneroPermission)
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
