
# Crea un programa que pida al usuario que ingrese una palabra o
# frase y determine si es un palíndromo. Un palíndromo es una palabra
# o frase que se lee igual de izquierda a derecha que de derecha a
# izquierda (ignorando espacios y mayúsculas).

texto = input("Ingresa una palabra o frase y determinaré si cada palabra es un palíndromo: ")

frase_minus = texto.lower()  # Convertir a minúsculas
palabras = frase_minus.split()  # Dividir en palabras

for palabra in palabras:
    if palabra == palabra[::-1]:
        print(f"{palabra} es un palíndromo")
    else:
        print(f"{palabra} no es un palíndromo")