class Monitor:

    contador_monitores = 0

    def __init__(self, marca, tamanio):
        Monitor.contador_monitores += 1
        self.__id_monitor = Monitor.contador_monitores
        self.__marca = marca
        self.__tamanio = tamanio

    @property
    def id_monitor(self):
        return self.__id_monitor

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def tamanio(self):
        return self.__tamanio

    @tamanio.setter
    def tamanio(self, tamanio):
        self.__tamanio = tamanio

    def __str__(self):
        return f'Monitor [ID: {self.__id_monitor}, Marca: {self.__marca}, Tamaño: {self.__tamanio}]'


if __name__ == '__main__':
    monitor1 = Monitor('ThinkVision', 'HDMI')
    print(monitor1)
    monitor2 = Monitor('Philips', 'VGA')
    print(monitor2)
