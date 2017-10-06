from django.contrib import admin
from .services import *

admin.site.register(Equipe)

def sorteio(modeladmin, request, queryset):
    sorteio = SorteioService()
    sorteio.sorteio()

sorteio.short_description = "Sorteio de Combinações"

admin.site.add_action(sorteio, 'Sortear Combinações')


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

@admin.register(Combinacao)
class CombinacaoAdmin(admin.ModelAdmin):

    list_filter = ('faixa', 'peso', 'idade')
    list_display = (
        'chave',
        'sexo',
        'faixa',
        'peso',
        'idade',
        'quantidade',
    )

    def quantidade(self, obj):
        return len(obj.inscricao.all())

@admin.register(Confronto)
class ConfrontoAdmin(admin.ModelAdmin):

    list_filter = ('confronto',)
    list_display = (
        'confronto',
        'faixa',
        'categoria_peso',
        'categoria_idade',
        'inscricao',
        'academia'
    )

    def academia(self, obj):
        return obj.inscricao.atleta.academia.nome

