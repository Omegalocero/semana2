#Crear un programa que se ingrese la edad del usuario en número y pueda
#calcular si es adolescente (edad entre 13 y 17 años).
Edad_minima = 13
Edad_maxima = 17
Edad = int(input("Ponga su edad aqui: "))
if Edad >= Edad_minima and Edad <= Edad_maxima:
    print("Usted es un adolecente")
else:
    print("Usted ya no es adolecente")