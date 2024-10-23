
# Crea un programa que pida al usuario un valor y un porcentaje a descontar.
# Luego, calcula el valor resultante después de restar ese porcentaje y, a
# continuación, suma ese mismo porcentaje al resultado. Finalmente, muestra
# los dos valores obtenidos y explica por qué el valor final no es igual al inicial.

valor = input("ingresa un valor: ")
porcentaje = input("ahora el porcentaje a descontar: ")

valor = float(valor)
porcentaje = float(porcentaje)

resultado_menos_porcentaje = valor - (porcentaje * valor / 100)
resultado_mas_el_porcentaje = resultado_menos_porcentaje + (porcentaje * resultado_menos_porcentaje / 100)

print(f"si al valor {valor} le descontamos {porcentaje}% da {resultado_menos_porcentaje:.2f}")
print(f" y si a {resultado_menos_porcentaje:.2f} le sumamos el {porcentaje}% queda {resultado_mas_el_porcentaje:.2f}")
print("esto es porque al restar un porcentaje cuando queremos sumar otra vez el mismo porcentaje al resultado este ya no es el 100%")