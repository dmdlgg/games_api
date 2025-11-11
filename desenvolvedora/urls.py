from django.urls import path
from desenvolvedora.views import ListCreateDevView, RetrieveUpdateDestroyDevView

urlpatterns = [

    path('desenvolvedoras/', ListCreateDevView.as_view(), name='desenvolvedora-create-list'),
    path('desenvolvedora/<int:pk>', RetrieveUpdateDestroyDevView.as_view(), name='desenvolvedoras-detail'),

]
