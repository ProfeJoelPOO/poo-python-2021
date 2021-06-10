from clase16.dispositivo_entrada import DispositivoEntrada


class Raton(DispositivoEntrada):

    contador_ratones = 0

    def __init__(self, marca, tipo_entrada):
        Raton.contador_ratones += 1
        self.__id_raton = Raton.contador_ratones
        super().__init__(marca, tipo_entrada)

    @property
    def id_raton(self):
        return self.__id_raton

    def __str__(self):
        return f'Raton: [ID: {self.__id_raton}], {super().__str__()}'


if __name__ == '__main__':
    raton1 = Raton('HP', 'USB')
    print(raton1)
    raton2 = Raton('Genius', 'Bluetooth')
    print(raton2)
