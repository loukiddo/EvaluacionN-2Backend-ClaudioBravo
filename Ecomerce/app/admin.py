from django.contrib import admin
from .models import Pelicula

class PeliculaAdmin(admin.ModelAdmin):
    list_display=('titulo', 'genero', 'precio', 'stock')
admin.site.register(Pelicula,PeliculaAdmin)