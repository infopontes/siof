from django.urls import include, path
from rest_framework import routers

from despesa.api.viewsets import DespesaViewSet, DespesaAutenticationView

app_name = 'despesa'

router = routers.DefaultRouter()

router.register(r'despesas', DespesaViewSet, basename='despesas')

from . import views

urlpatterns = [
    path('ptrab/', views.despesa_list, name='despesa_list'),
    #path('create/', v.despesa_create, name='despesa_create'),
    path('api/v1/', include(router.urls)),
    path('api/v1/despesa-autentication/', DespesaAutenticationView.as_view())
]