# Crea un programa que pida al usuario que ingrese una cadena de texto
# y luego cuente cuántas vocales (a, e, i, o, u) hay en esa cadena.
# Al final, muestra el resultado

texto = input("ingresa un texto: ")

vocales = "AaEeIiOoUu"
con_voc = 0

for caracteres in texto:
    if caracteres in vocales:
        con_voc += 1
        
print(f"hay {con_voc} vocales")