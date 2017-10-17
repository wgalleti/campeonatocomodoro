from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django_pandas.io import read_frame

from .services import *
from .models import Combinacao, CombinacaoAbsoluto

# Create your views here.


def index(request):
    return render(request, 'home.html')

def absoluto(request):
    a = CombinacaoAbsoluto.objects.all().order_by('sexo', 'faixa', 'idade')
    return render(request, 'absoluto.html', dict(absoluto=a))


def inscricao(request):
    c = Combinacao.objects.all().order_by('sexo', 'faixa', 'idade', 'peso')
    return render(request, 'inscricao.html', dict(combinacoes= c))

def resultado(request):
    ac = Resultado.objects.academia()[:5]
    eq = Resultado.objects.equipe()[:5]

    return render(request, 'resultado.html', {'academia': ac, 'equipe': eq})

@login_required(login_url='/admin')
def combinacao(request):

    combinacao = SorteioService()
    combinacao.combinacao()
    combinacao.combinacao_absoluto()

    messages.success(request, 'Inscrições processadas com sucesso!')

    return redirect('inscricao')
