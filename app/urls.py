from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('generos.urls')),
    path('api/v1/', include('diretores.urls')),
    path('api/v1/', include('jogos.urls')),
    path('api/v1/', include('reviews.urls')),
    path('api/v1/', include('autenticacao.urls')),
    path('api/v1/', include('desenvolvedora.urls')),
]
