#Escribir una función que encuentre el número más grande en una lista de números.

"""Definir una función encontrar_maximo que tome como argumento una lista de números.
Inicializar una variable maximo con el primer número de la lista.
Iterar sobre los números en la lista y actualizar maximo si se encuentra un número mayor.
Al finalizar la iteración, maximo contendrá el número más grande.
Imprimir el número más grande encontrado."""

lista = [100, 102, 200, 103]

def encontrar_maximo (lista):
    maximo = lista [0]
    for numero in lista:
        if numero > maximo:
            maximo = numero

    return (maximo)
                   
encontrar_maximo(lista)

print (encontrar_maximo (lista))




