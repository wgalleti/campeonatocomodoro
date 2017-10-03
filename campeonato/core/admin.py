from django.contrib import admin
from campeonato.core.models import *

admin.site.register(Equipe)

@admin.register(Academia)
class AcademiaAdmin(admin.ModelAdmin):

    list_display = ('nome', 'cidade', 'estado', 'equipe')
    list_filter = ('cidade', 'equipe')

@admin.register(Atleta)
class CadastroAdmin(admin.ModelAdmin):

    list_display = ('nome', 'sexo', 'idade', 'faixa')
    list_filter = ('sexo', 'faixa')
    search_fields = ('nome',)

@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):

    list_display = (
        'data',
        'atleta',
        'categoria_peso',
        'categoria_idade',
        'absoluto',
        'valor',
        'valor_absoluto'
    )
    list_filter = ('data', 'atleta__sexo', 'atleta__faixa', 'atleta__academia__nome', 'atleta__academia__equipe__nome')
    search_fields = ('nome', )

