class Orden:

    contador_ordenes = 0

    def __init__(self):
        Orden.contador_ordenes += 1
        self.__id_orden = Orden.contador_ordenes
        self.__computadoras = []

    @property
    def id_orden(self):
        return self.__id_orden

    def agregar_computadora(self, computadora):
        self.__computadoras.append(computadora)

    def __str__(self):
        computadoras_str = ''
        for elem in self.__computadoras:
            computadoras_str += elem.__str__()


        return f'''
        Orden
        [ID: {self.__id_orden},
        Computadoras: {computadoras_str}]
        '''
