# Escribe un programa que pida al usuario un número y luego imprima la tabla de
# multiplicar de ese número (del 1 al 10). El programa debe preguntar si desea
# ingresar otro número o salir.

dato = int(input("Ingresa un número: "))

def total(num):    
    almacena_total = []  # Almacena el primer valor
    for i in range(1, num + 1):
        a = dato * i # Multiplica por el valor ingresado en cada iteración
        almacena_total.append(a)
    return almacena_total  # Devolvemos la lista completa
    
resultado = total(10)
print(resultado)