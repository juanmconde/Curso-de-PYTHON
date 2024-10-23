
# creando una lista con la funcion list(no es muy comun) para crear o agregar una lista [] corchetes
lista = list(["pedro","gil","trabajador",22,True])
print(lista)

# len cuenta la cantidad de elementos de una lista o caracteres depende 
cadena = "Hola como va"
cuenta = len(cadena) # devuelve la cantidad de caracteres
print(cuenta)
cuenta1 = len(lista) # devuelve la cantidad de elementos que contiene la lista
print(cuenta1)

# agregando un elemento a la lista creada (agregamos directamente la lista un elemento)
lista.append("pepona")
print(lista)

# insert agregar un elemento a la lista en un indice especifico
lista.insert(3,"chupala")
print(lista)

#  extend agrega varios elementos a la lista, agregamos una lista a otra lista[]
lista.extend(["pepita la chota","mojon","parpadp",33])
print(lista)

# pop elimina un elemento de la lista por su indice, para eliminar el ultimo elemento de una lista se inserta -1
print(len(lista))
lista.pop(4)
print(lista)

print(len(lista))
lista.pop(-1) #seria el 33(-1 es el ultimo elemento)
print(lista)

# remove elimina un elemento de la lista por su valor
lista.remove("trabajador")
print(lista)

# clear elimina todo los valores de la lista, va a mostrar [] vacios

# lista.clear()
# print(lista)

lista_numerica = list([22,1,32,0.1,0,44,False,2,145,True]) #numerico no lleva apostrofes 

# sort ordena la lista ascendente, no funciona con listas con cadena de textos
lista_numerica.sort() # aqui primero cero luego False, 1 y True
print(lista_numerica)

lista_numerica.reverse() #fijese en el orden del indice ultimo False, penultimo True (reverse solo invierte la cadena en el estado que la encuentra)
print(lista_numerica)

# verificar si un elemento se encuentra en la lista
elemento_encontrado = lista_numerica.index(0.1)
print(elemento_encontrado)