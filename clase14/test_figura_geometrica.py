from clase_cuadrado import Cuadrado
from clase_rectangulo import Rectangulo
from clase_figura_geometrica import FiguraGeometrica

# No se puede instanciar una clase abstracta
# figura = FiguraGeometrica(80, 90)

cuadrado1 = Cuadrado(5, 'Negro')
print(str(cuadrado1.calcular_area()) + 'cm2')

rectangulo1 = Rectangulo(3, 10, 'Amarillo')
print(str(rectangulo1.calcular_area()) + 'cm2')

print(cuadrado1)
print(rectangulo1)

# Method Resolution Order
print(Cuadrado.mro())
