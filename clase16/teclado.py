from clase16.dispositivo_entrada import DispositivoEntrada


class Teclado(DispositivoEntrada):

    contador_teclados = 0

    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclados += 1
        self.__id_teclado = Teclado.contador_teclados
        super().__init__(marca, tipo_entrada)

    @property
    def id_teclado(self):
        return self.__id_teclado

    def __str__(self):
        return f'Teclado: [ID: {self.__id_teclado}], {super().__str__()}'


if __name__ == '__main__':
    teclado1 = Teclado('HP', 'USB')
    print(teclado1)
    teclado2 = Teclado('Logitec', 'USB')
    print(teclado2)
