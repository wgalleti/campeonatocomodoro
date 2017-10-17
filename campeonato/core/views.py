from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django_pandas.io import read_frame

from .services import *
from .models import Combinacao, CombinacaoAbsoluto

# Create your views here.


def index(request):
    return render(request, 'home.html')

def inscricao(request):
    c = Combinacao.objects.filter(idade__in=[5,6]).exclude(faixa__in=[16,17]).order_by('sexo', 'faixa', 'idade', 'peso')
    a = CombinacaoAbsoluto.objects.all().order_by('sexo', 'faixa', 'idade')
    return render(request, 'inscricao.html', {'combinacoes': c, 'absoluto': a})

def resultado(request):
    ac = Resultado.objects.academia()[:5]
    eq = Resultado.objects.equipe()[:5]

    return render(request, 'resultado.html', {'academia': ac, 'equipe': eq})

@login_required(login_url='/admin')
def combinacao(request):

    combinacao = SorteioService()
    combinacao.combinacao()

    messages.success(request, 'Inscrições processadas com sucesso!')

    return redirect('inscricao')

@login_required(login_url='/admin')
def combinacao_absoluto(request):

    combinacao = SorteioService()
    combinacao.combinacao_absoluto()

    messages.success(request, 'Inscrições processadas com sucesso!')

    return redirect('inscricao')
