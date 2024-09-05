#Pedir al usuario que ingrese un número y luego imprimir la tabla de multiplicar del 1 al 10 para ese número.


"""for i in range (1,10):
    num = int (input ("Ingrese el numero:") )
    resultado = (i * num) 
    print ((i), "x", (num), "=", (resultado))"""

numero = int(input("Ingrese un número: "))
print("Tabla de multiplicar de", numero)
for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)

