from django.contrib import admin

from .models import Ptrab

#from documento.models import Documento
#from tipoPtrab.models import TipoPtrab

@admin.register(Ptrab)
class PtrabAdmin(admin.ModelAdmin):
    list_display = ('numero', 'data', 'operacao')
    search_fields = ('numero', 'data')
    list_filter = ('data',)