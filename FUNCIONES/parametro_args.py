
# forma no optima para sumar mas de un valor
def suma(a,b,c):
    return a+b+c

resultado = suma(2,4,5)
print(resultado) 

# usando el parametro args() para sumar
def suma(*numeros): # el * es para decirle que esto va a ser una lista y sum() va a  sumar todo dentro de la variable, el parametro *numeros siempre al final
    return sum(numeros)

resultado = suma(3,6,14,9,19,2)
print(resultado)

# otro ejemplo con argrs (argumento) *
def suma(nombre,*numero): # ojo con las comas y elementos 
    return print(f"{nombre}, el total de numeros que tenes es: {sum(numero)}")

resultado = suma("juan",3,6,14,9,19,2) # cuidado con la posicion de la coma 

def suma_total(numeros):
    return sum([*numeros]) # lista[]

resultados = suma_total([2,4,13,6,55]) # los pasamos como lista[]
print(resultados)