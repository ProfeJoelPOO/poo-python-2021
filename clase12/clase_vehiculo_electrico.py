class VElectrico:
    def __init__(self, autonomia):
        self._autonomia = autonomia
        self._cargado = False

    @property
    def autonomia(self):
        return self._autonomia

    @autonomia.setter
    def autonomia(self, autonomia):
        self._autonomia = autonomia

    @property
    def cargado(self):
        return self._cargado

    def cargarEnergia(self):
        self._cargado = True

    def __str__(self):
        return 'Autonomia: ' + str(self._autonomia) + ' , Cargado: ' + str(self._cargado)
