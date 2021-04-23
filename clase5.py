# Ciclo while
# Permite ejecutar un bloque de código mientras se cumpla una condición

i = 0
while i < 3:
    print(i)
    i += 1
else:
    print('Fin ciclo while')

# Break and Continue
# Break: Al ejecutarse, se corta la ejecución del ciclo completamente
# Continue: al ejecutarse, se corta la ejecución del ciclo en esa iteración y pasa a la siguiente

for letra in 'Holanda':
    if letra == 'a':
        print(letra)
        break
else:
    print('Fin ciclo for')

# Uso de Range => Imprimir números pares
for i in range(6):
    if i%2 != 0:
        continue
    print(i)

i = 0

# iteración = repetición
while i < 10:
    i += 1
    if i == 5:
        continue
    print('Me gustan todos los números menos el 5, entonces muestro el número: ', i)

# Funciones o métodos
# Es un bloque de código que se define dentro de una programa
# y que debe ser llamado para que se ejecute

def mi_funcion():
    print('Ejecutando mi función')


mi_funcion()


# Parametro o argumento
# Parametro: Es una variable definida entre los paréntesis de la funcion
# Argumento: Es el valor enviado a función
def funcion_arg(nombre, apellido):
    print('El nombre recibido es: ', nombre)
    print('Y el apellido es: ', apellido)


funcion_arg('Joel', 'Rosenthal')


# Retornar un valor
def suma(a=0, b=0):
    return a + b


print(suma()) # Valores por defecto
print(suma(2, 4)) # Valores explícitos
