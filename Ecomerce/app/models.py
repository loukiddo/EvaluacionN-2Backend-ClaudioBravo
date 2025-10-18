from django.db import models

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    precio = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    stock = models.IntegerField()
    detalles = models.TextField()
    imagen = models.CharField(max_length=300)
    

    def __str__(self):
        return self.titulo
