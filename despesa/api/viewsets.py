from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework.views import APIView


# para autenticação da api
from rest_framework.authentication import (
    BasicAuthentication,
    SessionAuthentication,
    TokenAuthentication
)

from rest_framework.permissions import (
    BasePermission,
    DjangoModelPermissions,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)


from despesa.models import Despesa
from despesa.api.serializers import DespesaSerializer


class DespesaViewSet(viewsets.ModelViewSet):
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer
    authentication_classes = (BasicAuthentication, SessionAuthentication, TokenAuthentication)
    #permission_classes = (IsAuthenticated,)
    permission_classes = (DjangoModelPermissions,)

class DespesaAutenticationView(APIView):

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)