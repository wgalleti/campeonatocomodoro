from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^inscricao/', inscricao, name='inscricao'),
    url(r'^combinacao/', combinacao, name='combinacao'),
    url(r'^absoluto/', combinacao_absoluto, name='absoluto'),
]
