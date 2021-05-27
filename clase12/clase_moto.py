from clase_vehiculo import Vehiculo


class Moto(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.__haceWilly = False

    @property
    def haceWilly(self):
        return self.__haceWilly

    def hacerWilly(self):
        self.__haceWilly = True

    def __str__(self):
        return super().__str__() + ' , Hace willy: ' + str(self.__haceWilly)


miMoto = Moto('Honda', 'Titan')
miMoto.arrancar()
miMoto.acelerar()
miMoto.hacerWilly()
print(miMoto)
