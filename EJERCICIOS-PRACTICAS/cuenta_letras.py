
# Escribe un programa que pida al usuario ingresar una palabra. Luego, el programa debe mostrar cuántas veces aparece cada letra en la palabra.

palabra = input("Ingresa palabra: ")

conteo_letras = {}

for caracter in palabra:
    if caracter.isalpha():  # Verifica si es una letra
        caracter = caracter.lower()  # Convierte a minúsculas
        if caracter in conteo_letras:
            conteo_letras[caracter] += 1  # Incrementa el conteo
        else:
            conteo_letras[caracter] = 1  # Inicializa el conteo

print(conteo_letras)
