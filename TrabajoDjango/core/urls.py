from django.urls import path
from .views  import  listado_juegos, detalle_juegos , detalle_juego,crear_juegos, editar_juegos, Home

urlpatterns = [ 
    
    path('',  Home, name="Home"), 
    path('juegosLista',  listado_juegos, name="listado_juegos"), 
    path('juegos/categoria/<int:id>/',  detalle_juegos , name="detalle_juegos"),
     path('juego/detalles/<int:id>/',  detalle_juego , name="detalle_juego"),
     path('juego/crearJuego/',crear_juegos, name="crear_juegos"),
     path('juego/<int:id>/editar/',editar_juegos, name="editar_juegos"),
] 