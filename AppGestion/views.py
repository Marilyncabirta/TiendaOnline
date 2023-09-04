from django.shortcuts import render
from django.shortcuts import render, redirect
from AppGestion.models import Producto
from django.views.generic import ListView,UpdateView
from django.urls import reverse_lazy

# Create your views here.

class ProductoListView(ListView):
    model=Producto
    template_name='productos.html'
    def get_queryset(self):
        return Producto.objects.all()
    
    
# class ProductoListView(ListView):
#     model=Producto
#     template_name='productos.html'
#     def get_context_data(self,**kwargs):
#         contexto=super().get_context_data(**kwargs)
#         contexto["productos"]=Producto.objects.all()
#         return contexto
#     def get_queryset(self):
#         return Producto.objects.all()
    
class ProductoUpdateView(UpdateView):
    model=Producto
    template_name='AppGestion'
    fields=['precio_actual','stock_disponible']
    success_url=reverse_lazy('producto')

def insertarProducto(request):
    var_id=request.POST['id']
    var_nombre=request.POST['nombre']
    var_imagen1=request.POST['imagen1']
    var_precio=request.POST['precio']

    producto=Producto.objects.create(id=var_id,
                                     nombre=var_nombre,  
                                     imagen1=var_imagen1, 
                                     precio=var_precio)                                 
    return redirect('/')    

def eliminarProducto(request,prod_id):
    producto=Producto.objects.get(id=prod_id)  
    producto.delete()
    return redirect('/verProducto')
    
    
def modificarProducto(request,prod_id):
    producto=Producto(id=prod_id)
    producto.id=8
    producto.nombre='Zapatillas'
    producto.imagen1='imagenprod8.jpg'
    producto.precio=56
    return redirect('/')