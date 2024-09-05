"""Hacer un programa que le pida al usuario que ingrese su edad y su sexo,
si el usuario es mayor de edad y ademas es menor de 65 años le debe permitir
al usuario quedarse en el programa, en caso contrario el programa debe
detenerse. Si el sexo es masculino que el programa salude al usuario como 
un caballero y si el sexo es femenino que el programa salude al usuario como
una dama.
Para que el usuario ingrese su sexo hacer un menu con condiciones."""


edad = int(input("Ingresa tu edad: "))

if edad < 18 or edad > 65:
 print ("Acceso Denegado")
 exit ()
else:
 print 

sexo = int (input ("""Ingrese el numero de su sexo
                1) Masculino
                2) Femenino
                   Respuesta: """))

if sexo == 1:
 print (f"Bienvenido Caballero de {edad} años")
if sexo == 2:
  print (f"Bienvenida Dama de {edad} años")
if sexo == 0 or sexo > 2:
 print ("Vuelva a intentarlo")






