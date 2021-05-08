''' Ejercicio Clases:
1. Crear una clase Producto con los siguiente atributos:
    - codigo
    - nombre
    - precio
Crearle, su constructor, getter y setter y una funcion llamada calcular_total, donde le pasaremos
unas unidades y debe calcular el precio final.

2. Añadir una clase Pedido que tiene como atributos:
    - lista de productos
    - lista de cantidades
Añade la siguiente funcionalidad:
    - total_pedido = Muestra el precio final del pedido
    - mostrar_productos = Muestra los productos del pedido

3. Siguiendo con la clase Pedido, añade la siguiente funcionalidad:
    - aniadir_producto = le pasamos un producto y una cantidad,
    Debemos validar que el dato que nos pasen es correcto, es decir,
    que sea un Producto y que la cantidad sea valida. En caso de que no,
    devolver una exception.
    - eliminar_producto = Le pasamos el Producto a borrar, si existe, lo eliminamos.
    Si no existe devolver una excepción, indicándolo.
    Comprobar también, que es un Producto el elemento que se pasa por parámetro
'''

class Producto:

    def __init__(self, codigo, nombre, precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio

    @property # Otra forma de hacer un get
    def codigo(self):
        return self.__codigo

    @codigo.setter # Otra forma de hacer un set
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio):
        self.__precio = precio

    def calcular_total(self, unidades):
        return self.__precio * unidades

    def __str__(self): # Sobreescritura de método __str__
        return 'Codigo: ' + str(self.__codigo) + ', nombre: ' + self.__nombre + ', precio: ' + str(self.__precio)


class Pedido:

    def __init__(self):
        self.__productos = []
        self.__cantidades = []

    def aniadir_producto(self, producto, cantidad):
        if not isinstance(producto, Producto):
            raise Exception('Error al añadir Producto: Producto debe ser de la clase Producto')

        if not isinstance(cantidad, int):
            raise Exception('Error al añadir Producto: Cantidad debe ser un número')

        if cantidad <= 0:
            raise Exception('Error al añadir Producto: Cantidad debe ser positiva o mayor que cero')

        if producto in self.__productos:
            indice = self.__productos.index(producto)
            self.__cantidades[indice] += cantidad
        else:
            self.__productos.append(producto)
            self.__cantidades.append(cantidad)

    def eliminar_producto(self, producto):

        if not isinstance(producto, Producto):
            raise Exception('Error al eliminar Producto: Producto debe ser de la clase Producto')

        if producto in self.__productos:
            indice = self.__productos.index(producto)
            del self.__productos[indice]
            del self.__cantidades[indice]
        else:
            raise Exception('Error al eliminar Producto: El producto no existe')

    def total_pedido(self):
        total = 0

        for (p, c) in zip(self.__productos, self.__cantidades):
            total = total + p.calcular_total(c)

        return total

    def mostrar_productos(self):

        for (p, c) in zip(self.__productos, self.__cantidades):
            print('Producto: ' + p.nombre + ', Cantidad: ' + str(c))


p1 = Producto(1, 'Producto 1', 5)
p2 = Producto(2, 'Producto 2', 10)
p3 = Producto(3, 'Producto 3', 20)

pedido = Pedido()

try:

    pedido.aniadir_producto(p1, 3)
    pedido.aniadir_producto(p2, 5)
    pedido.aniadir_producto(p1, 5)
    pedido.aniadir_producto(p3, 2)

    print('Total pedido: ', str(pedido.total_pedido()))

    pedido.mostrar_productos()

    pedido.eliminar_producto(p3)

    print('Total pedido: ', str(pedido.total_pedido()))

    pedido.mostrar_productos()

except Exception as e:
    print(e)
