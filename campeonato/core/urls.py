from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^inscricao/', inscricao, name='inscricao'),
    url(r'^sorteio/', sorteio, name='sorteio'),
]
