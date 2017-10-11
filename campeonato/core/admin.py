from django.contrib import admin
from .services import *

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
    list_filter = (
    'data', 'atleta__sexo', 'atleta__faixa', 'atleta__academia__nome', 'atleta__academia__equipe__nome', 'absoluto')
    search_fields = ('nome',)


class CombateInfoInLine(admin.TabularInline):
    model = CombateInfo
    extra = 2


@admin.register(Combate)
class CombateAdmin(admin.ModelAdmin):
    inlines = (CombateInfoInLine,)

    list_display = (
        'chave',
        'data',
        'encerrada',
    )


@admin.register(CombateResultado)
class ResultadoAdmin(admin.ModelAdmin):
    list_display = (
        'combate',
        'atleta',
        'tipo_vitoria',
        'tempo'
    )


@admin.register(Chave)
class ChaveAdmin(admin.ModelAdmin):
    list_display = (
        'sexo',
        'faixa',
        'idade',
    )


@admin.register(Resultado)
class ResultadoAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'absoluto',
        'pontos',
        'descricao',
    )

    def nome(self, obj):
        return obj.atleta.atleta.nome