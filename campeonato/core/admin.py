from django.contrib import admin
from .services import *
from .exports import *
from import_export.admin import ImportExportModelAdmin


@admin.register(Equipe)
class EquipeAdmin(ImportExportModelAdmin):
    resource_class = EquipeResource
    list_display = ('nome',)


@admin.register(Academia)
class AcademiaAdmin(ImportExportModelAdmin):
    resource_class = AcademiaResource
    list_display = ('nome', 'cidade', 'estado', 'equipe')
    list_filter = ('cidade', 'equipe')


@admin.register(Atleta)
class CadastroAdmin(ImportExportModelAdmin):
    resource_class = AtletaResource
    list_display = ('nome', 'sexo', 'idade', 'faixa')
    list_filter = ('sexo', 'faixa', 'academia')
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
        'data', 'atleta__sexo', 'atleta__faixa', 'atleta__academia__nome', 'categoria_idade', 'absoluto')
    search_fields = ('atleta__nome',)


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
