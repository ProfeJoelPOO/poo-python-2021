from clase11 import Persona


def opciones():
    print('*' * 50)
    print('Opciones: ')
    print('1. Crear un objeto persona')
    print('2. Ver objetos personas creados')
    print('3. Seleccionar un objeto')
    print('0. Salir')
    print('*' * 50)


def opciones2():
    print('*' * 50)
    print('Opciones: ')
    print('1. ¿Es mayor de Edad?')
    print('2. Información acerca de su peso')
    print('3. Modificar nombre: ')
    print('4. Modificar sexo: ')
    print('0. Volver al menú anterior')
    print('*' * 50)


def main():
    personas = []
    opciones()
    option = int(input('Ingrese la opcion deseada: '))

    while option != 0:
        if option == 1:
            print('A continuación se solicitan los datos de la persona, press ENTER to skip')
            print('-'*10)
            personas.append(Persona(
                input('Ingrese el nombre: '),
                input('Ingrese el sexo (H/M): '),
                int(input('Ingrese la edad: ') or 0),
                float(input('Ingrese el peso: ') or 0.0),
                float(input('Ingrese la altura: ') or 0.0)
            ))
            print('Persona creada exitosamente!!')

        elif option == 2:
            for persona in personas:
                print(personas.index(persona), '-', persona)

        elif option == 3:
            indice = int(input('Ingrese el indice de la persona: '))
            while indice >= len(personas):
                indice = int(input('Ingrese el indice de la persona: '))

            opciones2()
            option2 = int(input('Ingrese la opcion deseada: '))

            while option2 != 0:
                if option2 == 1:
                    if personas[indice].esMayorDeEdad():
                        print('La persona ' + personas[indice].nombre + ' es mayor de edad')
                    else:
                        print('La persona ' + personas[indice].nombre + ' es menor de edad')

                elif option2 == 2:
                    imc = personas[indice].calcularIMC()
                    if imc == -1:
                        print('Esta bajo de peso')
                    elif imc == 0:
                        print('Su peso es el ideal')
                    else:
                        print('Tiene sobrepeso')

                elif option2 == 3:
                    personas[indice].nombre = input('Ingrese el nuevo nombre: ')

                elif option2 == 4:
                    personas[indice].sexo = input('Ingrese el nuevo sexo (H/M): ')

                opciones2()
                option2 = int(input('Ingrese la opcion deseada: '))

        opciones()
        option = int(input('Ingrese la opcion deseada: '))


main()
