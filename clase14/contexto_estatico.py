'''
Contexto estatico: Corresponde al contexto de definición de la clase
Contexto dinamico: Corresponde al contexto de instanciación de la clase o creación de objetos
Metodo estatico: No tiene información relacionada con la clase. Es decir, que se puede colocar como una
función dentro del archivo pero fuera clase y llamarla desde dentro tranquilamente. Pero sirve para
relacionar de manera lógica algún método que no tenga que ver con los atributos de nuestra clase pero que
si se relacionen con la clase de alguna manera lógica
Metodo asociado a la clase: Si recibe contexto de la clase. Por lo que recibe el parametro cls, que
hace referencia a la clase (no se usa class, porque class se usa para definir clases), y ya no es necesario
utilizar el nombre de la clase en este caso.
'''
class MiClase:

    variable_clase = 'Valor variable clase'

    def __init__(self, variable_intancia):
        self.variable_intancia = variable_intancia

    @staticmethod
    def metodo_estatico():
        print('Esto es un metodo estatico')
        print(MiClase.variable_clase)

    @classmethod
    def metodo_clase(cls):
        print('Esto es un metodo de clase')
        print(cls.variable_clase)

    def metodo_instancia(self):
        print('Esto es un metodo de instancia')


objeto1 = MiClase('Valor variable de intancia')
print(objeto1.variable_clase) # Desde el cont. dinamico si puedo acceder al cont. estatico
print(objeto1.variable_intancia)
print(MiClase.variable_clase)
# print(MiClase.variable_intancia) # Desde el contexto estatico no puedo acceder al cont. din.
MiClase.metodo_estatico()
# MiClase.metodo_instancia() # Desde el contexto estatico no puedo acceder al cont. din.
objeto1.metodo_instancia()
objeto1.metodo_estatico() # Desde el cont. dinamico si puedo acceder al cont. estatico
