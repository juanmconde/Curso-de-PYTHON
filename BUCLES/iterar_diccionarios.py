
diccionario = {
    "nombre":"juan",
    "apellido":"conde",
    "edad":40
}

#recorriendo diccionario con for/in para obtener clave y valor
for datos in diccionario:
    print(datos)#muestra solo la clave, no el valor dentro de ella
    
#recorriendo diccionario con for/in con .items mostrando clave y valor
for datos in diccionario.items():
    print(datos)
    
#forma de iterar todo el diccionario con key y value
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"en la clave: {key} esta el valor: {value}")