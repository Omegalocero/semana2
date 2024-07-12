#Crear un programa que solicite 5 números mediante prompt. Calcular la
#suma acumulada y el promedio de los números ingresados.
Numero_1 = int(input("Ingrese un numero "))
Numero_2 = int(input("Ingrese un numero "))
Numero_3 = int(input("Ingrese un numero "))
Numero_4 = int(input("Ingrese un numero "))
Numero_5 = int(input("Ingrese un numero "))

Suma = (Numero_1 + Numero_2 + Numero_3 + Numero_4 + Numero_5)
print("La suma total es: ", Suma)
Promedio = Suma // 5
print ("El promedio total es: ",Promedio)