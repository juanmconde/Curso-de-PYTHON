
#datos compuestos agrupan datos
#las listas entre[] se pueden modificar

lista = ["juan conde", "masculino", True, 1.83]
print(lista)

#para mostrar un dato es entre corchetes [1] va desde el 0 al 9

print(lista[1])

#los datos compuestos tupla ente() no se puede modificar una ves asignado el dato
#la tupla permite repetir valores

tupla = ("juan conde", "masculine", True, 2.22, "juan conde")
print(tupla)

#para mostrar los datos (print) siempre entre corchetes

#creando conjunto (set) con llaves {}
#no permite repetir valores
#no permite mostrar (print) por indice [1]
#no se accede a elementos por indice, no almacena datos duplicados y aparecen de forma desordenada al mostrarlos

conjunto = {"juan conde", "masculino", True, 1.83, "juan conde"}
print(conjunto)

#creando un diccionario (dict) la estructura es 'key' : "value" y se separa por comas

diccionario = {
    'nombre' : "juan",
    'apellido' : "conde",
    'edad' : "40",
    'sexo' : "masculino",
    'esta vivo' : True
}

print(diccionario["esta vivo"])

