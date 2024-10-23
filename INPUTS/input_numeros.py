
#pedir un numero

numero = input("meteme un numerito para multiplicarlo x 2: ")
resultado_texto = numero *2
print(resultado_texto)  #al ser variable texto va a devoler una repeticion del texto, hay que pararlo a variavle numero con int

numero2 = input("ahora si lo multiplico con int mandame otro numerito: ")
resultado_int = int(numero2) * 2
print(resultado_int)

#multiplicar con comas a traves de float
numero2 = input("ahora si lo multiplico con float mandame otro numerito con coma: ")
resultado_float = float(numero2) * 2
print(resultado_float)