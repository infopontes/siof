from django.contrib import admin


from .models import Despesa

@admin.register(Despesa)
class TipoDespesaAdmin(admin.ModelAdmin):
    list_display = ('data', 'tipo_despesa_id', 'unidade_id', 'nd', 'valor')
    search_fields = ('data', 'tipo_despesa_id')
    list_filter = ('data', 'tipo_despesa_id')
