from django.urls import include, path
from rest_framework import routers


from tipoDespesa.api.viewsets import TipoDespesaViewSet

app_name = 'tipodespesa'

router = routers.DefaultRouter()

router.register(r'tipodespesa', TipoDespesaViewSet, basename='tipodespesa')


urlpatterns = [
    path('api/v1/', include(router.urls)),
]