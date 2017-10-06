from .models import *


class SorteioService():


    def __init__(self):
        pass



    def sorteio(self):
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
                    inscricao.atleta.faixa,
                    inscricao.categoria_idade,
                    inscricao.categoria_peso
                )].append(inscricao)
            except KeyError:
                combinacoes[(
                    inscricao.atleta.sexo,
                    inscricao.atleta.faixa,
                    inscricao.categoria_idade,
                    inscricao.categoria_peso
                )] = [inscricao]

        for row in combinacoes:
            c = Combinacao(chave=row, sexo=row[0], faixa=row[1], idade=row[2], peso=row[3])
            c.save()
            c.inscricao.add(*combinacoes[row])