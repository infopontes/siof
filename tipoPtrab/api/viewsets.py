from rest_framework import viewsets

from tipoPtrab.models import TipoPtrab
from tipoPtrab.api.serializers import TipoPtrabSerializer


class TipoPtrabViewSet(viewsets.ModelViewSet):
    queryset = TipoPtrab.objects.all()
    serializer_class = TipoPtrabSerializer