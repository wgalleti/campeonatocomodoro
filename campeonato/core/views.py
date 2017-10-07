from django.shortcuts import render
from django.http import HttpResponse

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

    return HttpResponse('Ok')

