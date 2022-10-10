from django.contrib import admin


from .models import TipoDespesa

@admin.register(TipoDespesa)
class TipoDespesaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    list_filter = ('nome',)
