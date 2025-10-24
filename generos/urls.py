from django.urls import path
from . import views

urlpatterns = [

    path('generos/', views.GenerosListCreateView.as_view(), name='generos-create-list'),
    path('generos/<int:pk>/', views.GenerosRetrieveUpdateDestroyView.as_view(), name='generos-detail'),

]
