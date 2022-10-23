from django.contrib import admin


from .models import Despesa

@admin.register(Despesa)
class TipoDespesaAdmin(admin.ModelAdmin):
    list_display = ('tipo_despesa_id', 'unidade_id', 'nd', 'valor')
    search_fields = ('tipo_despesa_id',)
    list_filter = ('tipo_despesa_id',)
