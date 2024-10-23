
# llamar a un modulo con import
# cambie a la carpeta nueva_carpeta el modulo_saludar y asi lo llamamos
import nueva_carpeta.modulo_saludar 

saludo = nueva_carpeta.modulo_saludar.saludar_bien("jose")
print(saludo)

# importando un modulo y asignandole el nombre m_saludar
# import modulo_saludar as m_saludar

# desde este modulo llamamos dos funciones y les cambiamos el nombre
from nueva_carpeta.modulo_saludar import saludar_bien as saludar, saludar_raro as saludar_como_coscu

# para ver el nombre original se lo cambiamos 
import nueva_carpeta.modulo_saludar as m_saludar

saludo = saludar("pepino")
saludo_raro  = saludar_como_coscu ("bermellon")

print(saludo)
print(saludo_raro)

# con esto vemos el nombre original
print(m_saludar.__name__)
print(saludar.__name__)