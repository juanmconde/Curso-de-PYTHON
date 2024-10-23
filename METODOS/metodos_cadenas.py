
dato1 = "Hola como estas Juan"
dato2 = "55542"
dato3 = "esta, todo, junto, para, joder"

# metodo upper convierte todo el texto guardado o no, a mayusculas o "texto a poner en mayusculas".upper()
mayus = dato3.upper()
print(mayus)

#metodo lower hace lo opuesto a upper
minus = dato1.lower()
print(minus)

#capitalize la primera letra de las palabras en mayusculas
cap = dato1.capitalize()
print(cap)

#find encuentra la primera aparicion del valor especificado te dice la posicion donde la encuentra comienza desde 0, sino devuelve -1
encontrar = dato1.find("a")
print(encontrar)

#index encuentra la primera aparicion del valor especificado, sino devuelve una excepcion 
busca = dato1.index("s")
print(busca)

#isnumeric devuelve true si es numerico
numeri = dato2.isnumeric()
print(numeri)

#isalpha devuelve true si es alfanumerico
alfa =dato3.isalpha()
print(alfa)

#count devuelve el numero de coincidencia que hay en una cadena
contador = dato1.count("a")
print(contador)
print("----------------------------")
#len cuenta los caracteres de una cadena, len es una funcion y va primero
cuenta = len(dato3)
print(cuenta)

#startswith comienza con
comienza_con = dato3.startswith("e")
print(comienza_con)

print("REPLACE")
#replace remplaza por el valor ingresado
cambia = dato2.replace("5","3") # replace(" ", "") asi quito los espacios---------------------
print(cambia)

#split separa por el valor ingresado, crea una lista de lo que separamos
separada = dato3.split(",")
print(separada)
print(separada[2]) #asi buscamos en una lista