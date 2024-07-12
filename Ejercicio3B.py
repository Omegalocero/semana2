#Crear un programa que solicite al usuario que ingrese un número.
#Se deberá validar que se encuentre entre 0 y 9 inclusive. En caso no
#coincidir con el rango, volverlo a solicitar hasta que la condición se cumpla
Numero = -1
Numero < 0 or Numero > 9

while Numero < 0 or Numero > 9:
    Numero = int(input("Ingrese un numero entero: "))
    if Numero < 0 or Numero > 9:
        print("Su numero esta fuera del rango, ingrese nuevamente")
        int(input())
    else:
        print("Numero valido") 