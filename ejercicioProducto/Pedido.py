from Producto import Producto

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
