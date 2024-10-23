# Escribe un programa que pida al usuario una cadena de texto.
# El programa debe convertir esa cadena a mayúsculas y luego contar cuántas vocales (a, e, i, o, u) contiene

texto = input("escribe una cadena de texto: ")

texto_mayusculas = texto.upper()

vocales = "AEIOU"
contador_vocales = 0

for caracter in texto_mayusculas:
    if caracter in vocales:
        contador_vocales += 1

print("Número de vocales:", contador_vocales)
print(texto_mayusculas)