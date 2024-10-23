# Escribe un programa que pida al usuario un número entero y luego
# imprima si ese número es par o impar.

numero = input("ingresa un numero entero: ")
numero = int(numero)
if numero %2 == 0:
    print(f"es un numero par el: {numero}")
else:
    print(f"el numero {numero} es impar")