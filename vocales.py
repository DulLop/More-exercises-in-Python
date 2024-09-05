#Escribe un programa que cuente el número de vocales (mayúsculas y minúsculas) en una cadena de texto ingresada por el usuario.

palabra = input ("Ingrese un texto: ")


def contar_vocales ():
    vocales = "aeiou"
    contador = 0
    for letras in palabra:
        if letras in vocales:
            contador += 1

    print (contador)

contar_vocales()


    

