'''
Polimorfismo: Significa múltiples formas en tiempo de ejecución. Así que una misma variable
puede ejecutar varios métodos de distinto objetos dependiendo del objeto al cual está apuntado
en tiempo de ejecución.
'''


from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalle(objeto):
    print(type(objeto))
    print(objeto)


empleado = Empleado('Norberto', 50000)
gerente = Gerente('Manolo', 60000, 'Compras')

imprimir_detalle(empleado)
imprimir_detalle(gerente)
