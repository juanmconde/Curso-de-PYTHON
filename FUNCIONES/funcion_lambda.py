
# creando funcion que diga si es par o no

numeros = [0,1,2,3,4,5,6,7,8,9,10]

def es_par(num):
    if(num%2==0):
        return True

def es_impar(num):
    if(num%2==1):
        return True

# usando filter con una funcion comun, no se que filtra(hace recorrer la lista numeros 1 por 1)
todos_los_impares = filter(es_impar,numeros)
todos_los_pares = filter(es_par,numeros)

print(list(todos_los_pares))
print(list(todos_los_impares))

# con la funcion lambda es mas corto lo mismo que arriba para los pares hermoso
pares = filter(lambda num: num%2 == 0,numeros)
print(list(pares))