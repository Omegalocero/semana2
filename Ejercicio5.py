#Crear un programa que al ingresar un número puede calcular si es mayor,
#niño/a(menor de 10) o pre-adolescente (edad entre 10 y 13 años)
#adolescente (edad entre 13 y 17 años) de edad.
numero = int(input("Ingrese su edad "))
if numero < 10:
    print("Usted tiene:", numero,"años usted es es un niño.")
elif numero >= 10 and numero < 13: 
    print("Usted tiene", numero,"años usted es pre-adolesente")
elif numero >= 13 and numero < 17: 
    print("Usted tiene", numero,"años usted es adolesente")
else:
    print("Usted tiene",numero,"es mayor de edad")
