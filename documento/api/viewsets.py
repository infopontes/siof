from rest_framework import viewsets

from documento.models import Documento
from documento.api.serializers import DocumentoSerializer


class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer