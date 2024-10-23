
#creando diccionarios con dict() tambien pueden estar vacios
#no se pueden crear tuplas vacias, si con tuples
#no se pueden crear listas vacias salvo con list

diccionario = dict(nombre="juan",apellido="conde",edad="40")
print(diccionario)

#las listas no pueden ser claves las tuplas() pueden ser claves
#con listas[] dentro de {} tira error unhashable type : 'list'
#haciendo un conjunto{} tampoco
diccionario = {("dalto","rancio"):"jajaja"}
print(diccionario)

#metemos un frozenset{([])} para meter conjuntos

diccionario = {frozenset(["dalto","rancio"]):"jajaja"}
print(diccionario)

#creando diccionarios con fromkeys() con valores sin definir none
diccionario = dict.fromkeys(["nombre","apellido","edad"])
print(diccionario)

#ejemplo de diccionario con fromkeys() primer dato iterable segundo dato lo que vamos a igualar (meter) con fromkeys
diccionario = dict.fromkeys("123456","yes")
print(diccionario)

