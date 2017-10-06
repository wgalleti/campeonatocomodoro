from django.db import models

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
    peso = models.DecimalField(max_digits=15, decimal_places=2)
    faixa = models.IntegerField(choices=FAIXA, default=1)
    academia = models.ForeignKey('core.Academia')

    def __str__(self):
        return self.nome

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

    data = models.DateField()
    atleta = models.ForeignKey('core.Atleta')
    categoria_peso = models.IntegerField('Peso', choices=CATEGORIA_PESO, default=1)
    categoria_idade = models.IntegerField('Idade', choices=CATEGORIA_IDADE, default=5)
    absoluto = models.BooleanField(default=False)
    valor = models.DecimalField('valor da inscrição', max_digits=15, decimal_places=2, default=0, null=True, blank=True)
    valor_absoluto = models.DecimalField('valor absoluto', max_digits=15, decimal_places=2, default=0, null=True, blank=True)
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


class Confronto(models.Model):
    """
        Modelo de Confrontos
    """
    confronto = models.IntegerField()
    sexo = models.CharField(max_length=1, choices=Atleta.OPCAO)
    faixa = models.IntegerField(choices=Atleta.FAIXA)
    categoria_peso = models.IntegerField('Peso', choices=Inscricao.CATEGORIA_PESO, default=1)
    categoria_idade = models.IntegerField('Idade', choices=Inscricao.CATEGORIA_IDADE, default=5)
    inscricao = models.ForeignKey('core.Inscricao', verbose_name='inscrição')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{faixa}/{peso}/{idade}'.format(self.faixa, self.categoria_peso, self.categoria_idade)