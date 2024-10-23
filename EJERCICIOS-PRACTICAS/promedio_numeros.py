# Pide al usuario que ingrese varios números separados por un espacio.
# Luego, calcula y muestra: El número mayor. El número menor. El promedio de todos los números ingresados.
# Recordá que el usuario puede ingresar cualquier cantidad de números.

numeros = []

while True:
    valor = input("Ingresa números (s para salir): ")
    if valor == "s":
        break
    else:
        try:
            numeros.append(int(valor))  # Convertir a entero y agregar a la lista
        except ValueError:
            print("Por favor, ingresa un número válido.")

if numeros:  # Verificar si la lista no está vacía
    mayor = numeros[0]  # Inicializar con el primer número

    for n in numeros:
        if n > mayor:  # Comparar con el número mayor
            mayor = n

    print("El número mayor es:", mayor)
else:
    print("No se ingresaron números.")
