
# creando mi propia funcion
def saludo():
    print("Hola juan como estas hoy todo bien")

# llamando a la funcion
saludo()
saludo()

# crear funcion que contenga parametros
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "hombre"):
        adjetivo = "maquina"
    elif (sexo == "mujer"):
        adjetivo = "hermosa"
    elif (sexo == "no binario"):
        adjetivo = "mi amor"
    print(f"hola {nombre} como dice que le va {adjetivo}")

# definiendo la variable
saludar("pepa","mujer")

# crear una funcion que nos retorne multiples valores no va a ser random
def crear_contraseña_ramdom(num):
    chars = "sdgfolioe" # chars de caracteres
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num -3
    c2 = num
    c3 = num -5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num # con return se guarda el dato en la variable de otro modo funciona la funcion y lo imprimimos y se pierde
                      # de esta manera podemos trabajar con el dato que se guardo en la variable antes de mostrarlo
# desempaquetando la funcion
password,primer_nunero = crear_contraseña_ramdom(33214) # toma solo el primer numero porque[0] se lo pedimos podria ser el [1]segundo

print(f"tu contraseña vendria a ser: {password}")
print(f"el numero que usamos para crearla fue: {primer_nunero}")