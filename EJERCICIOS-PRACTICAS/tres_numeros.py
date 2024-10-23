
# Ejercicio: Escribe un programa que pida al usuario tres números enteros. 
# El programa debe mostrar cuál de los tres números es el mayor y cuál es el menor.

numeros = list()
numeros.append(int(input("ingresa el primer numero: ")))
numeros.append(int(input("ingresa el segundo numero: ")))
numeros.append(int(input("ingresa el tercer numero: ")))

numeros.sort()
print(numeros)