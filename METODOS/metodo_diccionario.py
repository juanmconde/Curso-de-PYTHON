
#metodo keys
diccionario = {
    "nombre" : "juan",
    "apellido" : "conde",
    "edad" : 40,
    "estado civil" : "desesperado"
}

#devuelve un dict_item (es un tipo de objeto que se puede iterar)

claves = diccionario.keys()
print(claves)

#metodo get

esta_en_diccionario_altura = diccionario.get("altura")  #con este metodo get si no encuentra el valor no sale un error y se para el programa solo nos muestra none
print(esta_en_diccionario_altura)

#eliminar todo el diccionario con .clear

#diccionario.clear()
#print(diccionario)

#eliminar un elemento del diccionario con .pop

diccionario.pop("estado civil")
print(diccionario)

#obteniendo elemento del dict con .items() iterable (recorrer el elemento para acceder a cada uno de esos elementos)

diccionario_iterable = diccionario.items()
print(diccionario_iterable)

