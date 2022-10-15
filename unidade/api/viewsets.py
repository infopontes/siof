from rest_framework import viewsets

from unidade.models import ComandoMilitarArea, RegiaoMilitar, Unidade
from unidade.api.serializers import ComandomilitarareaSerializer, RegiaomilitarSerializer, UnidadeSerializer


class ComandomilitarareaViewSet(viewsets.ModelViewSet):
    queryset = ComandoMilitarArea.objects.all()
    serializer_class = ComandomilitarareaSerializer


class RegiaomilitarViewSet(viewsets.ModelViewSet):
    queryset = RegiaoMilitar.objects.all()
    serializer_class = RegiaomilitarSerializer


class UnidadeViewSet(viewsets.ModelViewSet):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer