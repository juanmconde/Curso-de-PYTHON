animal = "   chanCHito feliz  "
print(animal.upper())
print(animal.lower())
# que el string no contenga un espacio en blanco al principio sino no funciona
print(animal.strip().capitalize())
print(animal.title())  # las palabras en mayusculas como un titulo
print(animal.strip())
print(animal.lstrip())  # saca los espacios en blanco del lado izq (left)
print(animal.rstrip())  # saca los del derecho (rigth)
print(animal.find("ch")) # diferencia mayus. y minus. si sale -1 es que no lo encontro. retorna en el indice donde se encuentra
print(animal.replace("nCH", "j"))
print("nCH" in animal) # devuelve valor booleano
print("nCH" not in animal) # booleano
