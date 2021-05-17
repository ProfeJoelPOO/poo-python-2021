from Descuento import Descuento
from Pedido import Pedido
from Producto import Producto

TIPO_DESC_FIJO = "Fijo"
TIPO_DESC_PORC = "Porcentaje"


## ---- Creación objetos descuento ----- ##
desc1 = Descuento('Fijo', 10)
desc2 = Descuento('Porcentaje', 40)


## ---- Creación objetos producto ----- ##
## p1:
##    Codigo: 1
##    Nombre: Producto 1
##    Precio: 5
##    Descuento: Fijo 10
## ---------------------------------
## p2:
##    Codigo: 2
##    Nombre: Producto 2
##    Precio: 10
##    Descuento: Porcentaje 40%
## ---------------------------------
## p3:
##    Codigo: 3
##    Nombre: Producto 3
##    Precio: 20
## ---------------------------------
p1 = Producto(1, 'Producto 1', 5, desc1)
p2 = Producto(2, 'Producto 2', 10, desc2)
p3 = Producto(3, 'Producto 3', 20)

pedido = Pedido()

try:

    pedido.aniadir_producto(p1, 3) ## 3 unidades del producto 1
    pedido.aniadir_producto(p2, 5) ## 5 unidades del producto 2
    pedido.aniadir_producto(p1, 5) ## 5 unidades del producto 1
    pedido.aniadir_producto(p3, 2) ## 2 unidades del producto 3

    print('Total pedido: ', str(pedido.total_pedido()))

    pedido.mostrar_productos()

    pedido.eliminar_producto(p3)

    print('Total pedido: ', str(pedido.total_pedido()))

    pedido.mostrar_productos()

except Exception as e:
    print(e)
