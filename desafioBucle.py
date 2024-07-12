secret_number = 777
print(
"""
+================================+
| ¡Bienvenido a mi juego, Junior!|
| Introduce un número entero |
| y adivina qué número he |
| elegido para ti. |
|¿Cuál es el número secreto? |
+================================+
""")

numero = int(input("Ingrese un numero entero "))

while numero != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    numero = int(input("Ingrese un numero entero "))
else:
    print("¡Bien hecho, Junior! Eres libre ahora.")
input("fin")
