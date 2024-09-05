#Ejercicio: Solicitar al usuario el radio de un círculo y calcular su área.

import math

def calcular (math, radio):
    return (math * radio ** 2)

math = math.pi
radio = float ( input ("Ingrese el radio del circulo:") )
print ("El area del circulo es:", calcular (math, radio))