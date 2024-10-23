# Ejercicio: Palabras más largas en una oración
# Pide al usuario que ingrese una oración.
# Encuentra la(s) palabra(s) más larga(s) en esa oración.
# Imprime la(s) palabra(s) más larga(s) y su longitud.


oracion = input("ingresa un texto: ")    
oracion_separada = oracion.split()

palabra_mas_larga = ""
for palabra in oracion_separada: # aca ya me va a ir tirando palabra por palabra la podria guardar en un diccionario o lista
    if len(palabra) > len(palabra_mas_larga):
        palabra_mas_larga = palabra
        
print(f"la palabra mas larga es: {palabra} con {len(palabra_mas_larga)} letras")