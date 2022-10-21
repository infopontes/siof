from django.contrib import admin
from django.urls import path, include, re_path

from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="SIOFI API",
        default_version='v1',
        description="API para integração entre sistemas de gestão financeira das operações.",
        terms_of_service="https://www.coter.eb.mil.br/policies/terms/",
        contact=openapi.Contact(email="mpontes@coter.eb.mil.br"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # para aparecer a tela de login e logout da api
    path('accounts/', include('django.contrib.auth.urls')),
    # urls da api
    path('', include('despesa.urls', namespace='despesa')),
    path('', include('documento.urls', namespace='documento')),
    path('', include('localidade.urls', namespace='localidade')),
    path('', include('ptrab.urls', namespace='ptrab')),
    path('', include('tipoDespesa.urls', namespace='tipodespesa')),
    path('', include('tipoPtrab.urls', namespace='tipoptrab')),
    path('', include('unidade.urls', namespace='unidades')),
    path('', include('core.urls', namespace='core')),
    # url das páginas
    #path('despesa/', include('despesa.urls')),
    path('unidade/', include('unidade.urls')),
    path('admin/', admin.site.urls),
]

# swagger
urlpatterns += [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),  # noqa E501
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # noqa E501
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # noqa E501
]