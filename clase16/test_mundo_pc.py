from clase16.computadora import Computadora
from clase16.monitor import Monitor
from clase16.orden import Orden
from clase16.raton import Raton
from clase16.teclado import Teclado


# monitor1 = Monitor('ThinkVision', 'HDMI')
# monitor2 = Monitor('Philips', 'VGA')
# teclado1 = Teclado('HP', 'USB')
# teclado2 = Teclado('Logitec', 'USB')
# raton1 = Raton('HP', 'USB')
# raton2 = Raton('Genius', 'Bluetooth')
# computadora1 = Computadora('Gamer', monitor1, teclado2, raton1)
# computadora2 = Computadora('Acer', monitor2, teclado1, raton2)
#
# orden1 = Orden()
# orden1.agregar_computadora(computadora1)
# orden1.agregar_computadora(computadora2)
# orden1.agregar_computadora(computadora1)
# print(orden1)

def opcionesMain():
    print('*' * 50)
    print('Opciones: ')
    print('1. Crear un objeto Monitor')
    print('2. Crear un objeto Teclado')
    print('3. Crear un objeto Raton')
    print('4. Crear un objeto Computadora')
    print('5. Crear un objeto Orden')
    print('6. Agregar computadoras a una orden')
    print('7. Mostrar objetos')
    print('0. Salir')
    print('*' * 50)

def opcionesMostrar():
    print('*' * 50)
    print('Opciones: ')
    print('1. Mostrar Monitores')
    print('2. Mostrar Teclados')
    print('3. Mostrar Ratones')
    print('4. Mostrar Computadoras')
    print('5. Mostrar Ordenes')
    print('0. Volver al menu anterior')
    print('*' * 50)

def main():
    monitores = []
    teclados = []
    ratones = []
    computadoras = []
    ordenes = []
    opcionesMain()
    opcionMain = int(input('Ingrese la opcion deseada: '))

    while opcionMain != 0:
        if opcionMain == 1:
            # Crear objetos monitor
            monitores.append(Monitor(
                input('Ingrese la marca del monitor: '),
                int(input('Ingrese el tamaño del monitor(num): '))
            ))
            print('Monitor creado exitosamente!!!')

        elif opcionMain == 2:
            # Crear objetos teclado
            teclados.append(Teclado(
                input('Ingrese la marca del teclado: '),
                input('Ingrese el tipo de entrada del teclado: ')
            ))
            print('Teclado creado exitosamente!!!')

        elif opcionMain == 3:
            # Crear objetos raton
            ratones.append(Raton(
                input('Ingrese la marca del raton: '),
                input('Ingrese el tipo de entrada del raton: ')
            ))
            print('Raton creado exitosamente!!!')

        elif opcionMain == 4:
            # Crear objetos computadora
            print('Las computadoras se componen de Raton, Teclado y Monitor, para ello debe elegir uno de cada uno')
            print('-' * 50)

            print('A continuación, se mostrará la lista de Ratones: ')
            for elem in ratones:
                print(ratones.index(elem), ' - ', elem)
            print('-' * 50)
            raton_elegido = int(input('Ingrese el indice del raton elegido: '))

            print('A continuación, se mostrará la lista de Teclados: ')
            for elem in teclados:
                print(teclados.index(elem), ' - ', elem)
            print('-' * 50)
            teclado_elegido = int(input('Ingrese el indice del teclado elegido: '))

            print('A continuación, se mostrará la lista de Monitores: ')
            for elem in monitores:
                print(monitores.index(elem), ' - ', elem)
            print('-' * 50)
            monitor_elegido = int(input('Ingrese el indice del monitor elegido: '))

            print('Ahora es tiempo de crear nuestra computadora: ')
            computadoras.append(Computadora(
                input('Ingrese el nombre de la computadora: '),
                monitores[monitor_elegido],
                teclados[teclado_elegido],
                ratones[raton_elegido]
            ))
            print('Computadora creada exitosamente!!!')

        elif opcionMain == 5:
            # Crear objetos orden
            ordenes.append(Orden())
            print('Orden creada exitosamente!!!')

        elif opcionMain == 6:
            # Agregar computadoras a orden
            print('Seleccionar orden a la cual deseo agregar la computadora')
            for elem in ordenes:
                print(ordenes.index(elem), ' - Orden nro', elem.id_orden)
            print('-' * 50)
            orden_elegida = int(input('Ingrese la orden deseada: '))
            print('Computadoras disponibles: ')
            for elem in computadoras:
                print(computadoras.index(elem), ' - ', elem.nombre)
            computadora_elegida = int(input('Ingrese la computadora elegida: '))
            ordenes[orden_elegida].agregar_computadora(computadoras[computadora_elegida])
            print('Computadora agregada correctamente!!!!')

        elif opcionMain == 7:
            # Mostrar opciones
            opcionesMostrar()
            opcion2 = int(input('Ingrese la opcion deseada'))

            while opcion2 != 0:
                if opcion2 == 1:
                    for elem in monitores:
                        print(elem)

                elif opcion2 == 2:
                    for elem in teclados:
                        print(elem)

                elif opcion2 == 3:
                    for elem in ratones:
                        print(elem)

                elif opcion2 == 4:
                    for elem in computadoras:
                        print(elem)

                elif opcion2 == 5:
                    for elem in ordenes:
                        print(elem)

                opcionesMostrar()
                opcion2 = int(input('Ingrese la opcion deseada'))

        opcionesMain()
        opcionMain = int(input('Ingrese la opcion deseada: '))


main()
