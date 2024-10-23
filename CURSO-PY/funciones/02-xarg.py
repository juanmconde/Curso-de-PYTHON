def suma(a, b, c):
    print(a + b + c)


suma(2, 5, 8)


def sumar(*numeros):  # el asterisco es para indicar que es iterable
    resultado = 0
    for numero in numeros: # recorre numeros
        resultado += numero # los va sumando y guardando
    print(f"El resultado es: {resultado}") # ojo con este print


sumar(2, 5, 3, 44, 2, 4, 3, 7, 9, 55, 5)
sumar(2, 5)
