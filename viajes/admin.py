from django.contrib import admin
from viajes.models import Destino, PaquetesTuristico

admin.site.register(Destino)
class destinoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais', 'precio')
    list_filter = ('pais',)
    search_fields = ('nombre', 'ciudad')

admin.site.register(PaquetesTuristico)
class paquetesTuristicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'destino', 'duracion', 'valor')
    list_filter = ('destino',)
    search_fields = ('nombre',)