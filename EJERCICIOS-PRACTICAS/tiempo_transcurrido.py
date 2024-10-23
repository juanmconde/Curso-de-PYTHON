
# cree un programa que pida nombre y edad y muestre cuantos años tendra dentro de 5 años
# Verifique que la edad ingresada es un número.
#Si no es un número, muestra un mensaje de error y vuelve a pedir la edad hasta que sea válida.

nombre = input("Ingresa tu nombre: ")
edad = input("Ahora tu edad: ")

# Mientras la edad no sea numérica, seguimos pidiendo al usuario que ingrese un número
while not edad.isnumeric():
    edad = input("No es un número, intenta otra vez: ")

# Ahora que sabemos que es un número, lo convertimos a entero
edad = int(edad)
edad = edad + 5
print(f"Dentro de 5 años {nombre} tendrá {edad} años.")
