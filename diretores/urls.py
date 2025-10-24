from django.urls import path
from . import views


urlpatterns = [

    path('diretores/', views.ListCreateDiretorView.as_view(), name='diretores-create-list'),
    path('diretores/<int:pk>/', views.RetrieveUpdateDestroyDiretorView.as_view(), name='diretores-detail'),

]
