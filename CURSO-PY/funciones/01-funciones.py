def hola(nombre, apellido = "Feliz"):
    print(f"Hola {nombre}")
    print("Ultimate python")
    print(f"Tu nombre es {nombre} y tu apellido {apellido}")


nombre = input("Ingresa tu nombre: ")
hola(nombre, "Conde") # la variable nombre es un parametro y cuando tiene un valor es un argumento
hola("chancho")

hola(apellido = "Argento", nombre = "Pepe") # esto sirve cuando no sabemos el orden de las variables en la funcion
