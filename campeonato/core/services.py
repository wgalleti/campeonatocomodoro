from .models import *
from datetime import datetime


class ConcertaCagada():
    __adulto_masculino = [
        dict(id=1, descricao='Galo', limite=57.5),
        dict(id=2, descricao='Pluma', limite=64),
        dict(id=3, descricao='Pena', limite=70),
        dict(id=4, descricao='Leve', limite=76),
        dict(id=5, descricao='Médio', limite=82.3),
        dict(id=6, descricao='Meio Pesado', limite=88.3),
        dict(id=7, descricao='Pesado', limite=94.3),
        dict(id=8, descricao='Super Pesado', limite=100.5),
        dict(id=9, descricao='Pesadíssimo', limite=200),
    ]
    __adulto_feminino = [
        dict(id=1, descricao='Galo', limite=48.5),
        dict(id=2, descricao='Pluma', limite=53.5),
        dict(id=3, descricao='Pena', limite=58.5),
        dict(id=4, descricao='Leve', limite=64),
        dict(id=5, descricao='Médio', limite=69),
        dict(id=6, descricao='Meio Pesado', limite=74),
        dict(id=7, descricao='Pesado', limite=79.3),
        dict(id=8, descricao='Super Pesado', limite=200),
    ]
    __pre_mirim = [
        dict(id=1, descricao='Galo', limite=14),
        dict(id=2, descricao='Pluma', limite=17),
        dict(id=3, descricao='Pena', limite=20),
        dict(id=4, descricao='Leve', limite=23),
        dict(id=5, descricao='Médio', limite=26),
        dict(id=6, descricao='Meio Pesado', limite=29),
        dict(id=7, descricao='Pesado', limite=32),
        dict(id=8, descricao='Super Pesado', limite=35),
        dict(id=9, descricao='Pesadíssimo', limite=200),
    ]
    __mirim = [
        dict(id=1, descricao='Galo', limite=22),
        dict(id=2, descricao='Pluma', limite=25),
        dict(id=3, descricao='Pena', limite=28),
        dict(id=4, descricao='Leve', limite=31),
        dict(id=5, descricao='Médio', limite=34),
        dict(id=6, descricao='Meio Pesado', limite=37),
        dict(id=7, descricao='Pesado', limite=40),
        dict(id=8, descricao='Super Pesado', limite=43),
        dict(id=9, descricao='Pesadíssimo', limite=200),
    ]
    __infantil = [
        dict(id=1, descricao='Galo', limite=30),
        dict(id=2, descricao='Pluma', limite=34),
        dict(id=3, descricao='Pena', limite=38),
        dict(id=4, descricao='Leve', limite=42),
        dict(id=5, descricao='Médio', limite=46),
        dict(id=6, descricao='Meio Pesado', limite=50),
        dict(id=7, descricao='Pesado', limite=54),
        dict(id=8, descricao='Super Pesado', limite=58),
        dict(id=9, descricao='Pesadíssimo', limite=200),
    ]
    __infanto_junevinil = [
        dict(id=1, descricao='Galo', limite=42),
        dict(id=2, descricao='Pluma', limite=46),
        dict(id=3, descricao='Pena', limite=50),
        dict(id=4, descricao='Leve', limite=54),
        dict(id=5, descricao='Médio', limite=58),
        dict(id=6, descricao='Meio Pesado', limite=62),
        dict(id=7, descricao='Pesado', limite=66),
        dict(id=8, descricao='Super Pesado', limite=70),
        dict(id=9, descricao='Pesadíssimo', limite=200),
    ]
    __juvenil = [
        dict(id=1, descricao='Galo', limite=51),
        dict(id=2, descricao='Pluma', limite=56),
        dict(id=3, descricao='Pena', limite=61),
        dict(id=4, descricao='Leve', limite=66),
        dict(id=5, descricao='Médio', limite=71),
        dict(id=6, descricao='Meio Pesado', limite=76),
        dict(id=7, descricao='Pesado', limite=81),
        dict(id=8, descricao='Super Pesado', limite=86),
        dict(id=9, descricao='Pesadíssimo', limite=200),
    ]

    def categoria_idade(self, idade):
        lista = [
            dict(id=1, limite=6),
            dict(id=2, limite=9),
            dict(id=3, limite=12),
            dict(id=4, limite=15),
            dict(id=7, limite=17),
            dict(id=5, limite=29),
            dict(id=6, limite=100)
        ]

        for row in lista:
            if idade <= row['limite']:
                return row['id']

    def categoria_peso(self, atleta):
        tabela = []
        idade = self.categoria_idade(atleta.idade)
        if atleta.sexo == 'M' and idade in [5, 6]:
            tabela = self.__adulto_masculino
        if atleta.sexo == 'F' and idade in [5, 6]:
            tabela = self.__adulto_feminino
        if idade == 1:
            tabela = self.__pre_mirim
        if idade == 2:
            tabela = self.__mirim
        if idade == 3:
            tabela = self.__infantil
        if idade == 4:
            tabela = self.__infanto_junevinil
        if idade == 7:
            tabela = self.__juvenil

        for row in tabela:

            if atleta.peso <= row['limite']:
                print('Aew Caraleo')
                return row['id']

    def processar(self, **kwargs):

        f = Atleta.objects.all()

        if kwargs.get('id') is not None:
            f = f.filter(id=kwargs.get('id'))

        for row in f:

            if row.idade == 0 or row.peso == 0:
                continue

            idade = self.categoria_idade(row.idade)
            peso = self.categoria_peso(row)

            CATEGORIA_PESO = (
                (1, 'Galo'),
                (2, 'Pluma'),
                (3, 'Pena'),
                (4, 'Leve'),
                (5, 'Médio'),
                (6, 'Meio Pesado'),
                (7, 'Pesado'),
                (8, 'Super Pesado'),
                (9, 'Pesadíssimo'),
            )

            Inscricao(
                data=datetime.now(),
                atleta=row,
                categoria_peso=peso,
                categoria_idade=idade,
                absoluto=False,
                valor=50,
                valor_absoluto=20,
                pago_inscricao=False,
                pago_absoluto=False
            ).save()


class AutoPreenchimento():
    def resultado(self):
        Resultado.objects.all().delete()

        for row in Inscricao.objects.all():
            Resultado(**dict(
                atleta_id=row.id,
                absoluto=False,
                pontos=0,
                descricao=' '
            )).save()

        for row in Inscricao.objects.filter(absoluto=True):
            Resultado(**dict(
                atleta_id=row.id,
                absoluto=True,
                pontos=0,
                descricao=' '
            )).save()


class SorteioService():
    def __init__(self):
        pass

    def combinacao_absoluto(self):
        """
        Gera as combinações para categoria absoluto
        """

        CombinacaoAbsoluto.objects.all().delete()

        comb = dict()

        for insc in Inscricao.objects.filter(absoluto=True):

            try:
                comb[(
                    insc.atleta.sexo,
                    insc.atleta.faixa_convertida,
                    insc.categoria_idade,
                )].append(insc)
            except KeyError:
                comb[(
                    insc.atleta.sexo,
                    insc.atleta.faixa_convertida,
                    insc.categoria_idade,
                )] = [insc]

        for row in comb:
            print(row)
            c = CombinacaoAbsoluto(chave=row, sexo=row[0], faixa=row[1], idade=row[2])
            c.save()
            c.inscricao.add(*comb[row])

    def combinacao(self):
        """
            Resgatas todas inscrições
            Gera as combinacoes de peso, idade e faixa
            Gera as aleatoriedades
        """

        Combinacao.objects.all().delete()

        combinacoes = dict()

        for inscricao in Inscricao.objects.all():
            try:
                combinacoes[(
                    inscricao.atleta.sexo,
                    inscricao.atleta.faixa_convertida,
                    inscricao.categoria_idade,
                    inscricao.categoria_peso
                )].append(inscricao)
            except KeyError:
                combinacoes[(
                    inscricao.atleta.sexo,
                    inscricao.atleta.faixa_convertida,
                    inscricao.categoria_idade,
                    inscricao.categoria_peso
                )] = [inscricao]

        for row in combinacoes:
            c = Combinacao(chave=row, sexo=row[0], faixa=row[1], idade=row[2], peso=row[3])
            c.save()
            c.inscricao.add(*combinacoes[row])
