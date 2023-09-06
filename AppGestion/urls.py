from django.urls import path
from AppGestion.views import ProductoListView,insertarProducto,eliminarProducto,modificarProducto,ProductoUpdateView

urlpatterns = [
    path('',ProductoListView.as_view() ,name='producto'),
    path('insertarProducto',insertarProducto ),
    path('eliminarProducto/<int:prod_id>',eliminarProducto, name='eliminar' ),
    path('modificarProducto/<int:prod_id>',modificarProducto ,name='modificar'),

  
]