from rest_framework import viewsets

from tipoDespesa.models import TipoDespesa
from tipoDespesa.api.serializers import TipodespesaSerializer


class TipoDespesaViewSet(viewsets.ModelViewSet):
    queryset = TipoDespesa.objects.all()
    serializer_class = TipodespesaSerializer