from django.contrib import admin

from .models import TipoPtrab

@admin.register(TipoPtrab)
class TipoPtrabAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    list_filter = ('nome',)