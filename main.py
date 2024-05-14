"""-----------------------------//opcion 1//-------------------------------------------"""
palabra = input("Palabra: ")
""""
import random

i = 0
caracter_anterior = " "
salida = " "

longitud = len(palabra)

while i <= longitud:
    i += 1
    caracter_aleatorio = random.choice(palabra)
    if caracter_aleatorio != caracter_anterior:
        salida += caracter_aleatorio
    caracter_anterior = caracter_aleatorio



print("Anagrama:", salida)
"""

"""----------------------------------//opcion 2//---------------------------------------"""

def generar_anagramas(palabra):
    if len(palabra) <= 1:
        return [palabra]

    anagramas = []
    for i in range(len(palabra)):
        resto = palabra[i]
        resto_anagramas = generar_anagramas(palabra[:i] + palabra[i+1:])
        for anagrama in resto_anagramas:
            anagramas.append(resto + anagrama)

    return anagramas

anagramas = generar_anagramas(palabra)
print(anagramas)