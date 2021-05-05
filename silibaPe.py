'''
Ejercicio Sílaba 'pe':

- Cargar por teclado un texto con finalización en punto .
- Palabras separas por un espacio en blanco
El programa debe:
    Determinar cuántas palabras tienen 3, 5 o 7 letras.
    - Contador palabras 3 letras
    - Contador palabras 5 letras
    - Contador palabras 7 letras
    - Suma de los 3 contadores
    Determinar la cantidad de palabras con más de tres letras, que tienen una vocal en la tercera letra
    - Contador palabras +3 letras, con vocal en la 3era
    Determinar el porcentaje de palabras que tienen sólo una o dos vocales sobre el total de palabras de texto
    - Contador de vocales por palabra
    - Contador de palabras con 1 vocal
    - Contador de palabras con 2 vocales
    - Suma de los contadores con 1 o 2 vocales
    - Contador de palabras general
    Determinar la cantidad de palabras que contienen más de una vez la sílaba "pe"
    - Contador de sílaba 'pe' por palabra
    - Contador de palabras que tengan más de 1 vez la sílaba 'pe'
'''


def calcular_porcentaje(valor, total):
    if total > 0:
        por = round(((valor * 100) / total), 2)
        print('El porcentaje de palabras con 2 vocales sobre el total de palabras del texto es: ', por)
    else:
        print('El porcentaje de palabras con 2 vocales sobre el total de palabras del texto es 0')


def isVocal(letra):
    vocales = 'aeiouAEIOUáéíóúÁÉÍÓÚ'
    return letra in vocales


def ingresarTexto():
    texto = 'Test'
    while (texto[-1] != '.'):
        texto = input('Ingrese el texto a analizar, finaliza con punto: ')

    return texto


def main():
    print('Analizar texto con letras pe')
    print('*' * 10)
    texto = ingresarTexto()

    con_pal_357_let = con_pal_vocal_3era = 0
    con_voc_x_pal = con_1_2_voc_x_pal = 0
    con_pal = con_let = 0
    con_sil_pe_x_pal = con_pal_sil_pe_more_than_1 = 0

    anterior = ''
    tiene_vocal_3era = False

    for letra in texto:
        if letra == ' ' or letra == '.':
            if con_let > 0:
                con_pal += 1
                if con_let == 3 or con_let == 5 or con_let == 7:
                    con_pal_357_let += 1
                if con_let > 3 and tiene_vocal_3era:
                    con_pal_vocal_3era += 1
                if con_sil_pe_x_pal >= 2:
                    con_pal_sil_pe_more_than_1 += 1
                if con_voc_x_pal == 1 or con_voc_x_pal == 2:
                    con_1_2_voc_x_pal += 1

            con_sil_pe_x_pal = 0
            con_voc_x_pal = 0
            tiene_vocal_3era = False
            con_let = 0
        else:
            con_let += 1
            if isVocal(letra):
                con_voc_x_pal += 1

                if con_let == 3:
                    tiene_vocal_3era = True

                if letra == 'e' and anterior == 'p':
                    con_sil_pe_x_pal += 1

        anterior = letra

    print('La cantidad de palabras con 3, 5 o 7 letras de longitud son:', con_pal_357_let)
    print('La cantidad de palabras con mas de 3 letras y una vocal en la tercera letra son: ', con_pal_vocal_3era)
    calcular_porcentaje(con_1_2_voc_x_pal, con_pal)
    print('La cantidad de palabras con mas de una sílaba \'pe\' es: ', con_pal_sil_pe_more_than_1)

main()
