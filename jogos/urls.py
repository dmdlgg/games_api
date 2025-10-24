from django.urls import path
from . import views

urlpatterns = [

    path('jogos/', views.ListCreateJogoView.as_view(), name='jogos-create-list'),
    path('jogos/<int:pk>', views.RetrieveUpdateDestroyJogoView.as_view(), name='jogos-detail'),
    path('jogos/stats/', views.JogosStatsView.as_view(), name='jogos-stats-view'),

]
