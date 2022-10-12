from django.contrib import admin

from .models import Estado, Cidade, Localidade

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'uf')
    search_fields = ('codigo', 'nome', 'uf')
    list_filter = ('nome',)

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome', 'estado_id__uf')
    list_filter = ('nome',)

@admin.register(Localidade)
class LocalidadeAdmin(admin.ModelAdmin):
    pass