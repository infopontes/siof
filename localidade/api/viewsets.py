from rest_framework import viewsets

from localidade.models import Estado, Cidade
from localidade.api.serializers import EstadoSerializer, CidadeSerializer


class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer


class CidadeViewSet(viewsets.ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer