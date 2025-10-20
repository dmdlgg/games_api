from django.urls import path
from . import views

urlpatterns = [

    path('reviews/', views.ListCreateReviewView.as_view(), name='review-create-list'),
    path('reviews/<int:pk>', views.RetrieveUpdateDestroyReviewView.as_view(), name='review-detail')

]