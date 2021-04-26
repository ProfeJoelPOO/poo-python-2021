class Rectangulo:
    # Self: Es la variable que almacena el valor del puntero que apunta al objeto en uso en memoria
    # La notación *parametro representa que se espera una tupla (elementos separados por coma) o que es opcional
    # La notación **parametro representa que se espera un diccionario (clave-valor en donde la clave comienza con una letra) o que es opcional
    def __init__(this, base, altura, otro, *val, **dic):
        this.base = base
        this.altura = altura
        this.otro_valor = otro
        this.valores = val
        this.diccionario = dic


    def calcular_area(self):
        return self.base * self.altura


base = int(input('Proporciona la base: '))
altura = int(input('Proporcia la altura: '))

rec1 = Rectangulo(base, altura, (2,4), 5,5,6,6,4,3,6)
print('Calculo de áre: ', rec1.calcular_area())
print('Tupla pasada por objeto tupla: ', rec1.otro_valor)
print('Tupla pasada por notación *tupla: ', rec1.valores)


rec2 = Rectangulo(3, 5, 'Hola', (2,6,9,8),5,4)
print(rec2.calcular_area())
print(rec2.otro_valor)
print(rec2.valores)

rec3 = Rectangulo(4, 8, 'otro')
print(rec3.calcular_area())
print(rec3.otro_valor)

rec4 = Rectangulo(2, 3, 'Otro2', 4,5,6, m='manzana', p='pera', j='jicama')
print(rec4.valores)
print(rec4.diccionario)
