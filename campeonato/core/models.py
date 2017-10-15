from django.db import models
from django.db.models import Q


class Equipe(models.Model):
    """
        Modelo de Equipes
    """

    nome = models.CharField(max_length=100)
    observacao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome


class Academia(models.Model):
    """
        Modelo de Academia
    """

    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    equipe = models.ForeignKey('core.Equipe')

    def __str__(self):
        return self.nome


class Atleta(models.Model):
    """
        Modelo de Cadastro
    """

    MASC = 'Masculino'
    FEMI = 'Feminino'

    # tupla
    OPCAO = (
        ('M', MASC),
        ('F', FEMI),
    )

    FAIXA = (
        (1, 'Branca'),
        (2, 'Cinza / Branca'),
        (3, 'Cinza'),
        (4, 'Cinza / Preta'),
        (5, 'Amarela Branca'),
        (6, 'Amarela'),
        (7, 'Amarela / Preta'),
        (8, 'Laranja / Branca'),
        (9, 'Laranja'),
        (10, 'Laranja / Preta'),
        (11, 'Verde / Branca'),
        (12, 'Verde'),
        (13, 'Verde / Preta'),
        (14, 'Azul'),
        (15, 'Roxa'),
        (16, 'Marrom'),
        (17, 'Preta'),
        (18, 'Vermelha / Preta'),
        (19, 'Vermelha / Branca'),
        (20, 'Vermelha'),
    )

    nome = models.CharField(max_length=100, null=True)
    sexo = models.CharField(max_length=1, choices=OPCAO)
    idade = models.IntegerField(null=True, blank=True)
    peso = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    faixa = models.IntegerField(choices=FAIXA, default=1)
    academia = models.ForeignKey('core.Academia')

    @property
    def faixa_convertida(self):
        # Valida Juvenio
        faixa = self.faixa if self.faixa > 13 else 1
        # Valida Marrom e preta
        faixa = faixa if faixa not in [16, 17] else 17
        return faixa

    def __str__(self):
        return self.nome


class InscricaoManager(models.Manager):
    def total_pago(self):
        total = 0
        queryset = self.get_queryset().filter(Q(pago_inscricao=True) or Q(pago_absoluto=True))

        for row in queryset:
            total += row.valor + row.valor_absoluto

        return total


class Inscricao(models.Model):
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

    CATEGORIA_IDADE = (
        (1, 'Pré-Mirin'),
        (2, 'Mirin'),
        (3, 'Infantil'),
        (4, 'Infanto Juvenil'),
        (7, 'Juvenil'),
        (5, 'Adulto'),
        (6, 'Master'),
    )

    objects = InscricaoManager()

    data = models.DateField()
    atleta = models.ForeignKey('core.Atleta')
    categoria_peso = models.IntegerField('Peso', choices=CATEGORIA_PESO, default=1)
    categoria_idade = models.IntegerField('Idade', choices=CATEGORIA_IDADE, default=5)
    absoluto = models.BooleanField(default=False)
    valor = models.DecimalField('valor da inscrição', max_digits=15, decimal_places=2, default=0, null=True, blank=True)
    valor_absoluto = models.DecimalField('valor absoluto', max_digits=15, decimal_places=2, default=0, null=True,
                                         blank=True)
    pago_inscricao = models.BooleanField('inscrição paga', default=False)
    pago_absoluto = models.BooleanField('absoluto pago', default=False)

    class Meta:
        verbose_name = 'inscrição'
        verbose_name_plural = 'incrições'

    def __str__(self):
        return self.atleta.nome


class Combinacao(models.Model):
    """
        Modelo de Possiveis confrotntos
    """

    chave = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1, choices=Atleta.OPCAO)
    faixa = models.IntegerField(choices=Atleta.FAIXA)
    idade = models.IntegerField(choices=Inscricao.CATEGORIA_IDADE)
    peso = models.IntegerField(choices=Inscricao.CATEGORIA_PESO)
    inscricao = models.ManyToManyField('core.Inscricao')

    class Meta:
        verbose_name = 'combinação'
        verbose_name_plural = 'combinações'

    def __str__(self):
        return str(self.chave)


class CombinacaoAbsoluto(models.Model):
    """
        Modelo de Possiveis combinações absoluto
    """

    chave = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1, choices=Atleta.OPCAO)
    faixa = models.IntegerField(choices=Atleta.FAIXA)
    idade = models.IntegerField(choices=Inscricao.CATEGORIA_IDADE)
    inscricao = models.ManyToManyField('core.Inscricao')

    class Meta:
        verbose_name = 'combinação absoluto'
        verbose_name_plural = 'combinações absoluto'

    def __str__(self):
        return str(self.chave)


class Chave(models.Model):
    """
    Modelo de chaves
    """
    sexo = models.CharField(max_length=1, choices=Atleta.OPCAO)
    faixa = models.IntegerField(choices=Atleta.FAIXA)
    idade = models.IntegerField(choices=Inscricao.CATEGORIA_IDADE)

    class Meta:
        verbose_name = 'chave'
        verbose_name_plural = 'chaves'

    def __str__(self):
        return '{}/{}/{}'.format(self.get_sexo_display(),
                                 self.get_faixa_display(),
                                 self.get_idade_display())


class Combate(models.Model):
    """
        Modelo de Combates
    """

    ETAPA = (
        (1, 'Oitava de Final'),
        (2, 'Quarta de Final'),
        (3, 'Semi de Final'),
        (4, 'Final'),
        (5, 'Outra'),
    )

    chave = models.ForeignKey('core.Chave')
    data = models.DateTimeField()
    tempo = models.TimeField()
    etapa = models.IntegerField(choices=ETAPA, default=5)
    inscricao = models.ManyToManyField('core.Inscricao', through='core.CombateInfo')
    encerrada = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'combate'
        verbose_name_plural = 'combates'

    def __str__(self):
        return '{}-{}'.format(str(self.chave), self.get_etapa_display())


class CombateInfo(models.Model):
    """
    Modelo de informação do Combate
    """

    combate = models.ForeignKey('core.Combate')
    inscricao = models.ForeignKey('core.Inscricao')
    ponto = models.IntegerField(default=0)
    vantagem = models.IntegerField(default=0)
    punicao = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'informações dos combates'
        verbose_name = 'informação do combate'

    def __str__(self):
        return self.inscricao.atleta.nome


class CombateResultado(models.Model):
    TIPO = (
        (1, 'Finalização'),
        (2, 'Pontuação'),
        (3, 'Desistencia'),
        (4, 'W.O'),
        (5, 'Outro')
    )

    combate = models.ForeignKey('core.Combate')
    atleta = models.ForeignKey('core.CombateInfo')
    tipo_vitoria = models.IntegerField(choices=TIPO, default=1)
    tempo = models.TimeField()

    class Meta:
        verbose_name = 'resultado do combate'
        verbose_name_plural = 'resultados dos combates'

    def __str__(self):
        return '{}-{}'.format(str(self.combate.chave), self.combate.get_etapa_display())


class Resultado(models.Model):
    atleta = models.ForeignKey('core.Inscricao')
    absoluto = models.BooleanField(default=False)
    pontos = models.IntegerField(default=0)
    descricao = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'resultados'
        verbose_name = 'resultado'
        unique_together = ('atleta', 'absoluto')

    def __str__(self):
        return self.atleta.atleta.nome
