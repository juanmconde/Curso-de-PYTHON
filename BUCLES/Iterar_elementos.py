
#todo esto funciona tanto para listas[] - tuplas() - conjuntos{}range no
animales = ["perro","gato","loro","buho"]
numeros = [3,42,55,7]

#recorriendo(iterando) la lista animales 
for animal in animales:
    print(f"la variable animal ahora es: {animal}")
    
#iterando en la lista numeros
for numero in numeros:
    resultado = numero * 2
    print(resultado)
    
#iterando dos listas del mismo tamaño al mismo tiempo con zip()
print("---------------zip()---------------")
for animal,numero in zip(animales,numeros):
    print(f"recorriendo la lista 1: {animal}")
    print(f"recorriendo la lista 2: {numero}")

#range() primer parametro donde arranco segundo donde termino, si colocamos un solo parametro (20) va desde 0 a 20
print("------range()-----------------")
for num in range(5,10):
    print(num)

#forma no optima de recorrer una lista (no funca en conjunto)
for num in range(len(numeros)):
    print(numeros[num])

#forma de recorrer una lista por su indice
print("--------enumarate()---------")
for num in enumerate(numeros):
    print(num)
    print(num[1]) 
    
#si queremos acceder al indice [0] si queremos acceder al valor [1]
for num in enumerate(numeros):
    indice = num [0]
    valor = num [1]
    print(f"el indice es: {indice} y el valor es {valor}")

#for in con else
print("-------if con else---------")
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("el bucle termino")