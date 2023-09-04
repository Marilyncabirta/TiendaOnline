from AppGestion.models import Producto

class Carrito:
    def __init__(self,request):
        self.request=request
        self.session=request.session
        carrito=self.session.get('carrito')
        if not carrito:
            self.session['carrito']={}
            self.carrito=self.session['carrito']
        else:
            self.carrito=carrito
            
    def agregar(self,producto):
        id=str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "id":producto.id,
                "nombre":producto.nombre,
                "precio":producto.precio,
                "cantidad":1,
                "subtotal":producto.precio
            }
        else:
            self.carrito[id]['cantidad']+=1
            self.carrito[id]['subtotal']+=producto.precio
        self.guardar_carrito()

    def sacar(self,producto):
        id=str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]['cantidad']-=1
            self.carrito[id]['subtotal']-=producto.precio
            if self.carrito[id]['cantidad'] <=0: 
                del self.carrito[id]
        self.guardar_carrito()
    
    def limpiar(self):
        self.session['carrito']={}
        self.session.modified=True


    def guardar_carrito(self):
        self.session['carrito']=self.carrito
        self.session.modified=True
        
        
        