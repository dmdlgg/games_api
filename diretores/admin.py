from django.contrib import admin
from diretores.models import Diretor


@admin.register(Diretor)
class DiretorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'data_nascimento', 'nacionalidade')
