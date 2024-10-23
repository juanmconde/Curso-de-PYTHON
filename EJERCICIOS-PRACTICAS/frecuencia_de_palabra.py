# Escribí un programa que tome una cadena de texto (una oración o párrafo),
# y cuente cuántas veces aparece cada palabra en esa cadena. Mostrá las palabras
# ordenadas por la cantidad de veces que aparecen, de mayor a menor.

texto = input("Ingrese un texto u oración: ")  # Pidiendo ingresar un texto u oración
separa_texto = texto.split()  # Separa el texto en palabras usando espacios como delimitadores

frecuencias_de_palabras = {}  # Creamos un diccionario para almacenar las frecuencias de cada palabra

for palabra in separa_texto:  # Recorremos cada palabra en la lista separada
    if palabra in frecuencias_de_palabras:  # Verificamos si la palabra ya está en el diccionario
        frecuencias_de_palabras[palabra] += 1  # Si está, aumentamos su contador en 1
    else:
        frecuencias_de_palabras[palabra] = 1  # Si no está, inicializamos su contador en 1

# Ordenamos el diccionario por frecuencia, de mayor a menor
frecuencias_ordenadas = sorted(frecuencias_de_palabras.items(), key=lambda x: x[1], reverse=True)
# key=lambda x: x[1] aca es para que tome el segundo valor esta clave y valor clave=palabra y valor=veces que se repitio
for palabra, frecuencia in frecuencias_ordenadas:  # Recorremos las palabras y sus frecuencias ordenadas
    print(f"La palabra '{palabra}' aparece {frecuencia} veces.")  # Imprimimos el resultado

