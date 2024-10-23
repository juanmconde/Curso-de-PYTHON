# Escribe un programa que pida al usuario una lista de números
# separados por comas (por ejemplo, "3,5,2,8"). El programa debe convertir
# esta lista de números en una lista de enteros, calcular la suma de todos
# los números y mostrar el resultado.

numeros = []
while True:
    valor = input("ingresa un numero, para salir s: ")
    if valor == "s":
        break
    else:
        numeros.append(int(valor))

suma_numeros = sum(numeros)
print(f"los numeros ingresados son: {numeros}")
print(f"la suma de todos da: {suma_numeros}")