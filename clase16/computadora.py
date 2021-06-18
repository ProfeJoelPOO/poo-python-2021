from clase16.monitor import Monitor
from clase16.raton import Raton
from clase16.teclado import Teclado


class Computadora:

    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self.__id_computadora = Computadora.contador_computadoras
        self.__nombre = nombre
        self.__monitor = monitor
        self.__teclado = teclado
        self.__raton = raton

    @property
    def nombre(self):
        return self.__nombre

    def __str__(self):
        return f'''
        Computadora
        [ID: {self.__id_computadora}, Nombre: {self.__nombre}
        Monitor: {self.__monitor}
        Teclado: {self.__teclado}
        Raton: {self.__raton}]
        '''


if __name__ == '__main__':
    monitor1 = Monitor('ThinkVision', 'HDMI')
    monitor2 = Monitor('Philips', 'VGA')
    teclado1 = Teclado('HP', 'USB')
    teclado2 = Teclado('Logitec', 'USB')
    raton1 = Raton('HP', 'USB')
    raton2 = Raton('Genius', 'Bluetooth')
    computadora1 = Computadora('Gamer', monitor1, teclado2, raton1)
    print(computadora1)
    computadora2 = Computadora('Acer', monitor2, teclado1, raton2)
    print(computadora2)
