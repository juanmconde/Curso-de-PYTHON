#solicitar al usuario que ingrese una frase
frase = input("Hola maquina redactame un texto y te saco algunas conclusiones: ")

#contar el numero de espacios que hay entre palabras para calcular el numero de palabras
#sumamos 1 al conteo de espacios para que nos de el total de palabras
num_palabras = frase.count(" ")
num_palabras = num_palabras + 1
tiempo_que_tardas = num_palabras  / 2
print(f"escribiste {num_palabras} palabras")
if tiempo_que_tardas <= 60:
    print(f"y tardarias {tiempo_que_tardas} segundos en decir: {frase}")
else:
    print(f"tardas {tiempo_que_tardas} segundos, para flaco tampoco te pedi un testamento")

#en este caso una persona es 30% mas rapida y tardaria
tiempo_dalto =  tiempo_que_tardas * 0.7
print(f"por otro lado dalto es un 30% mas rapido hablando el tardaria {tiempo_dalto} segundos")