#Crear un programa que pida al usuario un número y pueda calcular si es o
#no mayor de edad. Si es mayor de 18 se mostrará el mensaje “MAYOR” caso
#contrario “MENOR”.
Edad = int(input("Ponga su edad aqui: "))
if Edad >= 18:
    print("Usted tiene:", Edad, "años. Tiene permiso para acceder")
else:
    print("Usted es menor de edad, acceso denegado")
