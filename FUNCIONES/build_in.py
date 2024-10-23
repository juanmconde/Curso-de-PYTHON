
numeros = (12, 45, 3, 11, 5, 7)

# funcion max() solo con numeros
mayor = max(numeros)
print(mayor)

# funcion min()
menor = min(numeros)
print(menor)

# round() redondea a los decimales que querramos
numero = round(12.5722451, 3)
print(numero)

# funcion bool() retorna False si hay: 0 - False - none - empty de lo contrario retorna True
que_es = bool("")
print(f"Esto es {que_es}")
print("-----------")
# retorna True si todos los valores son verdaderos
resultado = all(["gdfs", True, 22,])
print(resultado)

# sum() sumo todos los valores de un iterable
total = sum(numeros)
print(total)
