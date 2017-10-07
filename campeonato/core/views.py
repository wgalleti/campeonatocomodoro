from django.shortcuts import render, redirect
from django.contrib import messages

from .services import SorteioService
from .models import Combinacao, CombinacaoAbsoluto

# Create your views here.


def index(request):
    return render(request, 'home.html')

def inscricao(request):
    c = Combinacao.objects.all().order_by('sexo', 'faixa', 'idade', 'peso')
    a = CombinacaoAbsoluto.objects.all().order_by('sexo', 'faixa', 'idade')
    return render(request, 'inscricao.html', {'combinacoes': c, 'absoluto': a})


def combinacao(request):

    combinacao = SorteioService()
    combinacao.combinacao()

    messages.success(request, 'Inscrições processadas com sucesso!')

    return redirect('inscricao')


def combinacao_absoluto(request):

    combinacao = SorteioService()
    combinacao.combinacao_absoluto()

    messages.success(request, 'Inscrições processadas com sucesso!')

    return redirect('inscricao')
