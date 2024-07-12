#Crear un programa que solicite al usuario que ingrese una letra. Se deberá
#validar que la letra sea ‘U’, ‘T’ o ‘N’ (en mayusculas).
#En caso no coincidir con ninguna de las letras, volver a solicitarla hasta que
#la condición se cumpla.
UTN = "U" or "T" or "N"
Letras = input("Ingrese una letra en mayuscula ")
while Letras != UTN:
    Letras = input("ingrese otra letra en mayuscula ")
if Letras == UTN:
    print(Letras)