from django.shortcuts import render
from django.http import HttpResponse

from .services import SorteioService

# Create your views here.


def sorteio(request):

    sorteio = SorteioService()
    sorteio.sorteio()

    return HttpResponse('Ok')

