from django.contrib import admin

from .models import ComandoMilitarArea, RegiaoMilitar, Unidade

@admin.register(ComandoMilitarArea)
class ComandoMilitarAreaAdmin(admin.ModelAdmin):
    list_display = ('abreviatura', 'nome')
    search_fields = ('abreviatura', 'nome')
    list_filter = ('abreviatura',)

@admin.register(RegiaoMilitar)
class RegiaoMilitarAdmin(admin.ModelAdmin):
    list_display = ('abreviatura', 'nome')
    search_fields = ('abreviatura', 'nome')
    list_filter = ('abreviatura',)
@admin.register(Unidade)
class UnidadeAdmin(admin.ModelAdmin):
    list_display = ('codug', 'autonomia', 'nome')
    search_fields = ('codug', 'autonomia', 'nome')
    list_filter = ('autonomia', 'rm')
