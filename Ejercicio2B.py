#Crear un programa que solicite al usuario que ingrese una contraseña
#mediante prompt.
#Comprobar que la contraseña ingresada sea ‘utn750’. En caso de no
#coincidir, volver a solicitarla hasta que coincidan

Contraseña = "utn750"
print("ingrese su contraseña")

Posible_Contraseña = input("")
while Posible_Contraseña != Contraseña:
    Contraseña = "utn750"
    print("Contraseña incorrecta, ingrese nuevamente")
    Posible_Contraseña = input("")
else: 
    print("Contraseña correcta. iniciando sesion...." )