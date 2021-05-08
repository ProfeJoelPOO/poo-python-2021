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

    __productos = []
    __cantidades = []

    def __init__(self, productos, cantidades):
        self.__productos = productos
        self.__cantidades = cantidades

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

print(p1) # Al imprimir el objeto se llama implicitamente el método __str__
print(p2)
print(p3)

productos = [p1, p2, p3]
cantidades = [5, 10, 2]

pedido = Pedido(productos, cantidades)

print('Total pedido: ', str(pedido.total_pedido()))
pedido.mostrar_productos()
