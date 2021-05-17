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
