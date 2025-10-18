from .models import Pelicula

def generos(request):
    generos = (Pelicula.objects.order_by()
               .values_list('genero', flat=True)
               .distinct())
    return {'generos_nav': generos}
