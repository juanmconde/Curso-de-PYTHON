#for in salteando un elemento o valor

frutas = ["durazno","pera","banana","manzana","kiwi","pelon"]
cadena = ("juan conde")
numeros = (2,3,5,7,12)

for fruta in frutas:
    if fruta == "kiwi":
       continue
    print(f"te vas a comer una terrible {fruta}")
else:
    print("el bucle termino------------------------")

#evitar que el bucle siga ejecutandose con el breake el else tampoco se ejecuta
for fruta in frutas:
    if fruta == "banana":
       break
    print(f"te vas a comer una terrible {fruta}")
else:
    print("el bucle termino")
    
#recorrer o iterar un texto letra por letra
for letra in cadena:
    print(letra)
    
#for in en una sola linea de codigo 
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)