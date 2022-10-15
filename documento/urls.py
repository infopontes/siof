from django.urls import include, path
from rest_framework import routers


from documento.api.viewsets import DocumentoViewSet

app_name = 'documento'

router = routers.DefaultRouter()

router.register(r'documentos', DocumentoViewSet, basename='documento')


urlpatterns = [
    path('api/v1/', include(router.urls)),
]