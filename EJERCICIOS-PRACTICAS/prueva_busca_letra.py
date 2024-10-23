
# buscar letra en el texto con lambda
oracion = ("agustin esta mirando un auto y me tiene las pelotas por el piso porque quiero aprender a programar en python y esta meta gritar")
palabras = oracion.split()
texto = ["pepe","agustin","juan","naty","mate","pan","banana","nene"]

letra = filter(lambda letras: "p" in letras, texto)
print(list(letra))

mi_palabra = filter(lambda mi_palabra: "s" in mi_palabra,palabras)
print(list(mi_palabra))