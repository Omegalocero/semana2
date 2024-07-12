#Crear un programa que a partir del ingreso de la altura de un
#basquetbolista determinar si es pivot o no. Para serlo el mismo deberá
#medir más de 1.80 metros
Altura = float(input("Ponga su altura aqui: "))
if Altura >= 1.80:
    print("Usted mide:", Altura, "felicidades usted puede ser un pivot")
else:
    print("Usted no mide lo necesario")
