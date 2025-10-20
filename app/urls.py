from django.contrib import admin
from django.urls import path, include
from generos.views import GenerosListCreateView, GenerosRetrieveUpdateDestroyView
from diretores.views import ListCreateDiretorView, RetrieveUpdateDestroyDiretorView
from jogos.views import ListCreateJogoView, RetrieveUpdateDestroyJogoView
from reviews.views import ListCreateReviewView, RetrieveUpdateDestroyReviewView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('generos.urls')),
    path('api/v1/', include('diretores.urls')),
    path('api/v1/', include('jogos.urls')),
    path('api/v1/', include('reviews.urls')),
    path('api/v1/', include('autenticacao.urls')),
    
]
