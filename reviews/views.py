from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from reviews.permissions import ReviewPermission

class ListCreateReviewView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, ReviewPermission)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class RetrieveUpdateDestroyReviewView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, ReviewPermission)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
