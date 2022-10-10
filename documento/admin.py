from django.contrib import admin

from .models import Documento

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'data', 'om')
    search_fields = ('numero', 'data', 'om')
    list_filter = ('data', 'om')
