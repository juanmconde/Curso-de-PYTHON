
# importando una funcion dentro de una carpeta y cambiando su nombre para que sea mas practico su uso
import nueva_carpeta.saludar as m_saludar
print(m_saludar.saludar("juancho"))

# ejemplo para llamar a un modulo de mas afuera de estas carpetas

import sys
print(sys) # quiere decir que es nativo de python este modulo

# print(sys()) los 2 parentesis despues de sys es para acceder a las funciones

# y para acceder a las propiedades asi, las muestra como tupla (que no se modifican)
print(sys.builtin_module_names) # muestra los modulos nativos de python asi no repetimos el nombre porque ellos tienen la prioridad

# como usar otro modulo que no esta en nuestra misma carperta
print(sys.path)

sys.path.append ("e:\\Desktop\\Curso de PYTHON\\CARPETA_DE_PRUEVAS")

import hola_pepe as saludo
print(saludo.hola("juan")) # estamos imprimiendo el modulo saludo ()le damos un valor a la funcion
 