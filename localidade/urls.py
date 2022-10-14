from django.urls import include, path
from rest_framework import routers


from localidade.api.viewsets import EstadoViewSet, CidadeViewSet

app_name = 'localidade'

router = routers.DefaultRouter()

router.register(r'estados', EstadoViewSet, basename='estados')
router.register(r'cidades', CidadeViewSet, basename='cidades')


urlpatterns = [
    path('api/v1/', include(router.urls)),
]