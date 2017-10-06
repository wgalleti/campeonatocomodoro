from django.conf.urls import url, include
from .views import sorteio

urlpatterns = [
    url(r'^sorteio/', sorteio, name='sorteio'),
]
