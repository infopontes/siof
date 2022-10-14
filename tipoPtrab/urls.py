from django.urls import include, path
from rest_framework import routers


from tipoPtrab.api.viewsets import TipoPtrabViewSet

app_name = 'tipoptrab'

router = routers.DefaultRouter()

router.register(r'tipoptrab', TipoPtrabViewSet, basename='tipoptrab')


urlpatterns = [
    path('api/v1/', include(router.urls)),
]