from rest_framework import viewsets

from ptrab.models import Ptrab
from ptrab.api.serializers import PtrabSerializer


class PtrabViewSet(viewsets.ModelViewSet):
    queryset = Ptrab.objects.all()
    serializer_class = PtrabSerializer