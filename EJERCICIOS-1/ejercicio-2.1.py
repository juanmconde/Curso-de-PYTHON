
# 1 alumno es profesor
# 1 alumno es asistente
# A- pedir los datos de los compañeros que vinieron hoy a clase y ordenarlos de menor a mayor
# B- el mayor es el profesor y el menor es el asistente 

def pedir_datos():
    compañeros = []
    cantidad = int(input("¿Cuántos compañeros vinieron hoy a clase? "))

    # Pedimos los nombres y edades de los compañeros
    for i in range(cantidad):
        nombre = input(f"Nombre del compañero {i+1}: ")
        edad = int(input(f"Edad de {nombre}: "))
        compañero = (nombre, edad)
        compañeros.append(compañero)

    # Ordenamos los compañeros por edad (de menor a mayor)
    compañeros.sort(key=lambda x: x[1])

    # El menor es el asistente y el mayor es el profesor
    asistente = compañeros[0]
    profesor = compañeros[-1]

    return asistente, profesor

# Llamamos a la función y asignamos los valores retornados
asistente, profesor = pedir_datos()

print(f"El asistente es {asistente[0]} con {asistente[1]} años.")
print(f"El profesor es {profesor[0]} con {profesor[1]} años.")
