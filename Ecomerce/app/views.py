from django.shortcuts import render, get_object_or_404
from django.db.models import Count, Min
from .models import Pelicula

def main(request):
    genero_activo = request.GET.get('genero')  # filtro desde la navbar
    peliculas = Pelicula.objects.all()
    if genero_activo:
        peliculas = peliculas.filter(genero=genero_activo)

    # por si quieres usar la lista en otros lugares
    generos = (Pelicula.objects.order_by()
               .values_list('genero', flat=True)
               .distinct())

    context = {
        'peliculas': peliculas,
        'genero_activo': genero_activo,
        'generos': generos,
    }
    return render(request, 'main.html', context)

def detalles_pelicula(request, id):
    pelicula = get_object_or_404(Pelicula, pk=id)
    return render(request, 'detalles.html', {'pelicula': pelicula})

def genero(request, genero):
    peliculas = Pelicula.objects.filter(genero=genero)
    return render(request, 'genero.html', {'peliculas': peliculas, 'genero': genero})


