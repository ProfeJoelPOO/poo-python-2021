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
