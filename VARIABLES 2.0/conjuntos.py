#creando un conjunto con set()
conjunto = set(["dato1","dato2","dato3"])  #[]es para lista

#metiendo un conjunto en otro conjunto
conjunto1 = frozenset(["dato1","dato2"])
conjunto2 = {conjunto1,"dato3"}

print(conjunto2)

#teoria de conjuntos

conjunto1 = {1,3,5,7,9}
conjunto2 = {1,3,5,7,9}

#verificando si conjunto2 es un subconjunto de conjunto1
resultado = conjunto2.issubset(conjunto1)
print(resultado)
resultado = conjunto2 <= conjunto1 #otra forma de comprovar si es un subconjunto
print(resultado)

#verificar si es un superconmjunto
resultado = conjunto1.issuperset(conjunto2)
print(resultado)
resultado = conjunto1 > conjunto2
print(resultado)

#verificar si hay algun numero en comun 
resultado = conjunto1.isdisjoint(conjunto2) #devuelve False si hay algun numero igual dentro de los conjuntos ingresados
print(resultado)
