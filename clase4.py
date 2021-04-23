# Ejercicio 4

VOCALES = 'aeiouAEIOU'
texto = input('Ingrese el texto a analizar, separado por espacios en blanco y termina en punto: ')

cont_palabras = cont_letras = cont_empieza_vocal = cont_empieza_ultima = 0
empieza_vocal = False
ult_car_pal = car_ant = caracter = ''

for caracter in texto:
    if caracter == ' ' or caracter == '.':
        # Fin de palabra
        if cont_letras > 0:
            cont_palabras += 1
            ult_car_pal = car_ant
            if empieza_vocal and car_ant in VOCALES:
                cont_empieza_vocal += 1
                empieza_vocal = False
        cont_letras = 0

    else:
        # Dentro de la palabra
        cont_letras += 1
        if cont_letras == 1:
            if caracter in VOCALES:
                empieza_vocal = True
            if ult_car_pal == caracter:
                cont_empieza_ultima += 1
                ult_car_pal = ''

        car_ant = caracter


if cont_palabras > 0:
    porcentaje = cont_empieza_vocal * 100 / cont_palabras

    print('Hay', cont_empieza_vocal, 'palabras que empiezan y terminan en '
                                     'vocales que representan el', porcentaje,
                                     '% de palabras del texto')
    print('Hay', cont_empieza_ultima, 'palabras que comienzan con el último '
                                      'caracter de la palabra anterior')
else:
    print('No se ingresó texto a analizar')
