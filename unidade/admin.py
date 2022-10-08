from django.contrib import admin

from .models import ComandoMilitarArea, RegiaoMilitar, Unidade

# Register your models here.
admin.site.register(ComandoMilitarArea)
admin.site.register(RegiaoMilitar)
admin.site.register(Unidade)
