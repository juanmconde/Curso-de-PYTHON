n1 = input("ingresa primer numero: ")
n2 = input("ingresa segundo numero: ")
n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
divide = n1 / n2
multi = n1 * n2

mensaje = f"""
para los numeros {n1} y {n2},
el resultado de la suma es: {suma},
el resultado de la resta es: {resta},
el de la division es: {divide},
y la multiplicacion es: {multi}
"""

print(mensaje)