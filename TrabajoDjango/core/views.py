from django.shortcuts import render,redirect
from .models import  Juego,Categoria_Juego
from django.shortcuts import get_object_or_404
# Create your views here. 
def Home(request): 
    Categorias_Juegos = Categoria_Juego.objects.all() 
    contexto = { "Categorias_Juegos": Categorias_Juegos } 
    return render(request, 'juego/index.html', contexto )  
  
def listado_juegos(request): 
    Categorias_Juegos = Categoria_Juego.objects.all()
    juegos= Juego.objects.all()
    contexto = { "juegos":juegos, "Categorias_Juegos":Categorias_Juegos } 
    return render(request, 'juego/todosJuegos.html', contexto )  

def detalle_juegos(request, id): 
    Juegos = Juego.objects.filter(categoria_juego = id) 
    #juegos= Juego.objects.all() 
    contexto = { "Juegos":Juegos} 
    return render(request, 'juego/juegoCategoria.html', contexto )

def detalle_juego(request, id): 
    juegos = get_object_or_404(Juego, id=id  )
    Juegos = Juego.objects.filter(id = id) 
    #juegos= Juego.objects.all() 
    contexto = { "Juegos":Juegos} 
    return render(request, 'juego/juegoDetalle.html', contexto )

def crear_juegos(request ):
    if request.method== 'POST': 
        categoria_id = request.POST.get('categoria')
        categoria_juego = get_object_or_404(Categoria_Juego, id=categoria_id)
        
        precio = request.POST.get('precio')
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        imagen = request.POST.get('imagen')
        Juego.objects.create(
            precio = precio,
            nombre = nombre,
            descripcion = descripcion,
            imagen = imagen,
            categoria_juego = categoria_juego 
        )    
        
        return redirect( 'listado_juegos') 

    categorias = Categoria_Juego.objects.all()
    contexto = {  "categorias":categorias } 
    return render(request, 'juego/crearJuego.html', contexto )

def editar_juegos(request, id): 
    juego = get_object_or_404(Juego, id=id  )
    if request.method== 'POST':  
        categoria_id = request.POST.get('categoria')
        categoria_juego = get_object_or_404(Categoria_Juego, id=categoria_id) 
        juego.nombre = request.POST['nombre']
        juego.precio = request.POST['precio']
        juego.descripcion = request.POST.get('descripcion')
        juego.categoria_juego = categoria_juego 
        if 'imagen' in request.FILES : 
            juego.imagen = request.FILES ['imagen']  
        juego.save() 
           
    categoria_juegos = Categoria_Juego.objects.all()
    contexto = {  "juego":juego,  "categoria_juegos":categoria_juegos} 
    return render(request, 'juego/editarJuego.html', contexto )