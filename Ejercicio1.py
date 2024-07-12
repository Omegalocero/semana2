#Crear un programa que pida al usuario un número, si coincide con el valor 18, mostrar el mensaje “Usted tiene 18 años”.
Edad = int(input("Ponga su edad aqui: "))
if Edad == 18:
    print("Usted tiene:", Edad, "años. Tiene permiso para acceder")
else:
    print("Usted es menor de edad o no tiene la edad requerida, acceso denegado")