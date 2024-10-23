# con el numero ingresado dar una lista de los numeros primos

def es_primo(num):
    for i in range(2,num-1):
        if num%i == 0: return False
    return True

def primos_hasta(num):
    primos = []
    for i in range(3,num+1):
        resultado = es_primo(i)
        if resultado == True: primos.append(i)
    return primos
    
resultado = primos_hasta(101)
print(resultado)