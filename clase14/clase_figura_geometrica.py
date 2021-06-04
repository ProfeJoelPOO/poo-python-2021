# ABC = Abstract Base Class
'''
Las clases abstractas sirven de soporte para la definición de métodos que van
a ser implementados en cada una de las clases hijas que hereden de la clase
abstracta y que se relaciones lógicamente de FiguraGeométrica
'''
from abc import abstractmethod, ABC


class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        self._alto = alto

    @abstractmethod
    def calcular_area(self):
        pass

    def __str__(self):
        return f'FiguraGeometrica[ancho: {self._ancho}, alto: {self._alto}]'
