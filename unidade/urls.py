from django.urls import include, path
from rest_framework import routers

from unidade.api.viewsets import ComandomilitarareaViewSet, RegiaomilitarViewSet, UnidadeViewSet


#from unidade import views as v

app_name = 'unidade'

router = routers.DefaultRouter()

router.register(r'cmdomilarea', ComandomilitarareaViewSet, basename='cmdomilarea')
router.register(r'regiaomilitar', RegiaomilitarViewSet, basename='regiaomilitar')
router.register(r'unidades', UnidadeViewSet, basename='unidade')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    #path('', v.unidade_list, name='unidade_list'),
]