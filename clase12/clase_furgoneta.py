from clase_vehiculo import Vehiculo


class Furgoneta(Vehiculo):
    def __init__(self, marca, modelo, carga):
        super().__init__(marca, modelo)
        self.__cargado = self.__cargar(carga)

    @property
    def cargado(self):
        return self.__cargado

    @cargado.setter
    def cargado(self, carga):
        self.__cargado = self.__cargar(carga)

    def __cargar(self, carga):
        if carga:
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no tiene carga"

    def __str__(self):
        return super().__str__() + ' , Carga: ' + self.__cargado


miFurgoneta = Furgoneta('Ford', 'F100', False)
print(miFurgoneta)
