"""Hacer un programa que le pida al usuario que ingrese su edad y su sexo,
si el usuario es mayor de edad y ademas es menor de 65 años le debe permitir
al usuario quedarse en el programa, en caso
contrario el programa debe deternese. Si es sexo es masculino que el programa
salude al usuario como un caballero y si el sexo es femino que el programa salude al
usuario como una dama
-Para que el usuario ingrese su sexo hacer un menu con condiciones."""


edad = int (input ("Ingrese su edad:" ))
if edad < 18 or edad > 65:
     print ("No puede ingresar")
     exit ()

menu = int (input ("""Ingrese su sexo:
1) Mujer
2) Hombre
>>> : """))

if menu == 1:
    print ("Hello woman")
elif menu == 2:
    print ("Hello man")
elif menu > 2 or menu == 0:
    print ("Invalid option")






         