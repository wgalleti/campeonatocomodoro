from .models import *

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