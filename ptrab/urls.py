from django.urls import include, path
from rest_framework import routers


from ptrab.api.viewsets import PtrabViewSet

app_name = 'ptrab'

router = routers.DefaultRouter()

router.register(r'ptrab', PtrabViewSet, basename='ptrab')


urlpatterns = [
    path('api/v1/', include(router.urls)),
]