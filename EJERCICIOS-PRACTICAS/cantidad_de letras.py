# Crea un programa que pida al usuario una cadena de texto y cuente cuántas
# veces aparece cada letra en la cadena. Imprime el resultado en formato de
# diccionario, donde las llaves son las letras y los valores son las cantidades de apariciones.

texto = input("tipea una cadena de texto please: ")

lista_del_texto = []
abcedario = "abcdefghijklmnñopqrstuvwxyz"
contador = 0
for i in texto:
    if i in abcedario:
        contador += 1
        lista_del_texto.append(i)
        
conteo_letras = {}  # Inicializa el diccionario vacío

for caracter in texto:
    if caracter.isalpha():  # Verifica si el carácter es una letra
        if caracter in conteo_letras:
            conteo_letras[caracter] += 1  # Incrementa el conteo
        else:
            conteo_letras[caracter] = 1
            
ordenado_por_repeticion = sorted(conteo_letras.items(), key=lambda x: x[1], reverse=True)

print("Conteo de letras (de mayor a menor):")
for letra, conteo in ordenado_por_repeticion:
    print(f"{letra}: {conteo}")
    