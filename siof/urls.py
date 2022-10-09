from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls', namespace='core')),
    path('unidade/', include('unidade.urls', namespace='unidade')),
    path('admin/', admin.site.urls),
]
