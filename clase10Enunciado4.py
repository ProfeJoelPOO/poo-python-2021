'''
4. Crea una clase Descuento que tiene los siguientes atributos:
	- tipo: es un string y solo puede ser Fijo o Porcentaje
	- valor: es un numero, si es fijo debe ser mayor que 0 y si es porcentaje el valor debe estar entre 1 y 100.
Tiene la siguiente funcionalidad:
	- aplicar_descuento(precio):
		- Si el tipo es Fijo, se le resta la cantidad al precio
		- Si el tipo es Porcentaje, se le resta el porcentaje al precio
Añadir este descuento al producto, este sera opcional y solo se aplicara si tiene descuento.
Validar que el descuento se crea correctamente
'''

TIPO_DESC_FIJO = "Fijo"
TIPO_DESC_PORC = "Porcentaje"


class Producto:

    def __init__(self, codigo, nombre, precio, descuento=None):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
        self.__descuento = descuento

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
        if self.__descuento == None:
            return self.__precio
        else:
            return self.__descuento.aplicar_descuento(self.__precio)

    @precio.setter
    def precio(self, precio):
        self.__precio = precio

    def calcular_total(self, unidades):
        return self.precio * unidades

    # Objetivo del método str: Retornar un string con los atributos de la clase
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


class Descuento:

    def __init__(self, tipo, valor):
        if not isinstance(valor, int):
            raise Exception('Error: El valor debe ser de tipo Integer')

        if not isinstance(tipo, str):
            raise Exception('Error: El tipo debe ser de tipo String')

        if tipo != 'Fijo' and tipo != 'Porcentaje':
            raise Exception('Error: El descuento debe ser Fijo o Porcentaje')

        if tipo == 'Fijo' and valor <= 0:
            raise Exception('Error: El descuento fijo debe ser mayor que cero')

        if tipo == 'Porcentaje' and valor < 0 or valor > 100:
            raise Exception('Error: El descuento por porcentaje debe estar entre 0 y 100')

        self.__tipo = tipo
        self.__valor = valor

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    def aplicar_descuento(self, precio):
        if self.__tipo == 'Fijo':
            if precio > self.__valor:
                return precio - self.__valor
            else:
                return 0
        else:
            return precio - (precio * (self.__valor / 100))


desc1 = Descuento('Fijo', 10)
desc2 = Descuento('Porcentaje', 40)

p1 = Producto(1, 'Producto 1', 5, desc1)
p2 = Producto(2, 'Producto 2', 10, desc2)
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
