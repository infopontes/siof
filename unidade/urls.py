from django.urls import path

from unidade import views as v

app_name = 'unidade'

urlpatterns = [
    path('', v.unidade_list, name='unidade_list'),
]