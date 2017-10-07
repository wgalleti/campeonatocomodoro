from django.shortcuts import render, redirect
from django.contrib import messages

from .services import SorteioService
from .models import Combinacao

# Create your views here.


def index(request):
    return render(request, 'home.html')

def inscricao(request):
    c = Combinacao.objects.all().order_by('sexo', 'faixa', 'idade', 'peso')
    return render(request, 'chaves.html', {'combinacoes': c})

def sorteio(request):

    sorteio = SorteioService()
    sorteio.sorteio()

    messages.success(request, 'Inscrições processadas com sucesso!')

    return redirect('inscricao')

