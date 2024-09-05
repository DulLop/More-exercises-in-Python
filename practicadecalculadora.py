def sumar ( num1, num2 ):
  return (num1 + num2)

def restar ( num1 , num2):
  return (num1 - num2)

def dividir ( num1 , num2):
  return (num1 / num2)

def multiplicar ( num1 , num2):
  return (num1 * num2)

def programa ():
  menu = int (input ("""
1) Sumar
2) Restar
3) dividir
4) Multiplicar
5) Salir del programa
>>>  """))
  
  if menu ==1:
    num1 = int (input (f"Digita el primer numero que quieres sumar:  "))
    num2 = int (input (f"Digita el segundo numero que quieres sumar:  "))
    resultado = sumar (num1, num2)
    print (input (f"El resultado de la suma es: {resultado}"))

  elif menu == 2:
    num1 = int (input (f"Digita el primer numero que quieres restar:  "))
    num2 = int (input (f"Digita el segundo numero que quieres restar:  "))
    resultado = restar (num1, num2)
    print (input (f"El resultado de la resta es: {resultado}"))

  elif menu == 3:
    num1 = int (input (f"Digita el primer numero que quieres dividir:  "))
    num2 = int (input (f"Digita el segundo numero que quieres dividir:  "))
    resultado = dividir (num1, num2)
    print (input (f"El resultado de la division es: {resultado}"))

  elif menu == 4:
    num1 = int (input (f"Digita el primer numero que quieres multiplicar:  "))
    num2 = int (input (f"Digita el segundo numero que quieres multiplicar:  "))
    resultado = multiplicar (num1, num2)
    print (input (f"El resultado de la multiplicacion es: {resultado}"))

  elif menu == 5:
    print ("Hasta pronto")
    exit ()

  else:
    print ("Opcion invalida")  

while True:
    programa ()


