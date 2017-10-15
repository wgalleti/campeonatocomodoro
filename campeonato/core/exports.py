from import_export import resources
from .models import *


class EquipeResource(resources.ModelResource):
    """
        Resource do modelo de Equipes
    """

    class Meta:
        model = Equipe

class AcademiaResource(resources.ModelResource):
    """
        Resource do modelo Academia
    """

    class Meta:
        model = Academia


class AtletaResource(resources.ModelResource):
    """
        Resource do modelo Atleta
    """

    class Meta:
        model = Atleta
