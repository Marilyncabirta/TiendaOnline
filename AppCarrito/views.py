from django.shortcuts import render,redirect
from AppGestion.models import Producto
from AppCarrito.Carrito import Carrito
from django.views.generic import DetailView

# Create your views here.
def tienda(request):
    productos=Producto.objects.all().order_by('-id')
    return render(request,'tiendaonline.html',{'productos':productos})

def agregar_producto(request,prod_id):
    carrito=Carrito(request)
    producto=Producto.objects.get(id=prod_id)
    carrito.agregar(producto)
    return redirect('tienda')

def sacar_producto(request,prod_id):
    carrito=Carrito(request)
    producto=Producto.objects.get(id=prod_id)
    carrito.sacar(producto)
    return redirect('tienda')

def limpiar_carrito(request):
    carrito=Carrito(request)
    carrito.limpiar()
    return redirect('tienda')

class ProductoDetailView(DetailView):
    model=Producto
    template_name='descripcionProducto.html'
    def get_object(self):
        objeto=self.model.objects.get(id=self.kwargs['prod_id'])
        return objeto