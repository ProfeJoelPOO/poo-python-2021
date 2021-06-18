from recuperatorio_parcial1 import *


def menu():
    cuentas = []

    opcion = input("Ingrese 1 para crear una cuenta: \n"
                   "Ingrese 2 para hacer un ingreso de dinero: \n"
                   "Ingrese 3 para hacer un reintegro de dinero: \n"
                   "Ingrese 4 para hacer una transferencia de dinero: \n"
                   "Ingrese 5 para mostrar las cuentas: ")

    while opcion != "0":

        if opcion == "1":
            nombre = input("Ingrese el nombre de la cuenta: ")
            numero_cuenta = input("Ingrese el numero de cuenta: ")
            tipos_interes = input("Ingrese el tipo de interes: ")
            saldo = float(input("Ingrese el saldo de la cuenta: "))

            cuenta = Cuenta(nombre, numero_cuenta, tipos_interes, saldo)
            cuentas.append(cuenta)

        elif opcion == "2":
            cuenta_lista_ingreso = int(input("¿A que cuenta de la lista desea ingresarle dinero? (el primer elemento de"
                                             "la misma es el '0': "))

            ingreso = float(input("¿Que cantidad desea ingresar a la cuenta?: "))
            if cuentas[cuenta_lista_ingreso].ingreso(ingreso):
                print('Ingreso correcto')
            else:
                print('Ingreso fallido')

        elif opcion == "3":
            cuenta_lista_reintegro = int(input("¿A que cuenta de la lista desea retirarle dinero? (el primer elemento"
                                               "de la misma es el '0': "))

            reintegro = float(input("¿Que cantidad desea retirar de la cuenta?: "))

            if cuentas[cuenta_lista_reintegro].reintegro(reintegro):
                print('Reintegro correcto')
            else:
                print('Reintegro fallido')

        elif opcion == "4":
            cuenta_lista_origen = int(input("¿A que cuenta de la lista desea retirarle dinero? (el primer elemento"
                                               "de la misma es el '0': "))

            cuenta_lista_destino = int(input("¿A que cuenta de la lista desea retirarle dinero? (el primer elemento"
                                               "de la misma es el '0': "))

            transferencia = float(input("¿Que cantidad desea transferir de la cuenta?: "))

            if cuentas[cuenta_lista_origen].tranferir(cuentas[cuenta_lista_destino], transferencia):
                print('Transferencia correcta')
            else:
                print('Transferencia fallida')


        elif opcion == "5":
            for cuenta in cuentas:
                print(cuenta.__str__())
                print("--------------------")

        opcion = input("Ingrese 1 para crear una cuenta: \n"
                       "Ingrese 2 para hacer un ingreso de dinero: \n"
                       "Ingrese 3 para hacer un reintegro de dinero: \n"
                       "Ingrese 4 para hacer una transferencia de dinero: \n"
                       "Ingrese 5 para mostrar las cuentas: \n"
                       "Ingrese 0 para salir: ")


menu()
