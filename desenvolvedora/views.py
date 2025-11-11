from desenvolvedora.models import Desenvolvedora
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from app.permissions import ViewPermission
from desenvolvedora.serializers import DesenvolvedoraSerializer


class ListCreateDevView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, ViewPermission)
    queryset = Desenvolvedora.objects.all()
    serializer_class = DesenvolvedoraSerializer


class RetrieveUpdateDestroyDevView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, ViewPermission)
    queryset = Desenvolvedora.objects.all()
    serializer_class = DesenvolvedoraSerializer
