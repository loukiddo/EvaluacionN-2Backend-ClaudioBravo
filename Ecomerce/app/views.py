from django.shortcuts import render, get_object_or_404
from django.db.models import Count, Min
from .models import Pelicula

def main(request):
    genero_activo = request.GET.get('genero') 
    peliculas = Pelicula.objects.all()
    if genero_activo:
        peliculas = peliculas.filter(genero=genero_activo)

    
    generos = (Pelicula.objects.order_by()
               .values_list('genero', flat=True)
               .distinct())

    context = {
        'peliculas': peliculas,
        'generos': generos,
        'genero_activo': genero_activo,
    }
    return render(request, 'main.html', context)

def detalles_pelicula(request, id):
    pelicula = get_object_or_404(Pelicula, pk=id)
    context = {'pelicula': pelicula}
    return render(request, 'detalles.html', context)

def genero(request, genero):
    peliculas = Pelicula.objects.filter(genero=genero)
    context = {'peliculas': peliculas, 'genero': genero}
    return render(request, 'genero.html', context)
