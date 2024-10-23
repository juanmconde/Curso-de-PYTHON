def get_product(**datos):
    print(datos)


get_product(id="33")


def dicionario_datos(**datos): # dos ** para KeyWordarg()
    print(datos)
    print(datos["nombre"], datos["dni"])

dicionario_datos(dni="32323232",
                 nombre="pepe",
                 apellido="jose antonio rivero") # nombre del parametro - argumento se lo pasamos como diccionario
