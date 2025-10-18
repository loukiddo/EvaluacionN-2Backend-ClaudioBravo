from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('producto/<int:id>/', views.detalles_pelicula, name='detalles'),
    path('genero/<str:genero>/', views.genero, name='genero'),
]
