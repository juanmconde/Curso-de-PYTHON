
#duraciones cursos

otros_cursos_max = 7
otros_cursos_min = 2.5
otros_cursos_prom = 4
curso_soydalto = 1.5

crudo_prom = 5
crudo_soydalto = 3.5
#diferencias de duraciones

diferencia_con_min = 100 - curso_soydalto / otros_cursos_min * 100
diferencia_con_max = 100 - curso_soydalto * 1000 / otros_cursos_max  / 10
diferencia_con_prom = 100 - curso_soydalto / otros_cursos_prom * 100

#calculando el porcentaje de tiempo cvacio removido
tiempo_vacio_promedio = 100 - otros_cursos_prom * 1000 / crudo_prom / 10 
tiempo_vacio_soydalto = 100 - curso_soydalto * 1000 / crudo_soydalto / 10

#ejercicio A
print(f"el super curso de dalto dura un {diferencia_con_min} % menos que el mas rapido")
print(f"el super curso de dalto dura un {diferencia_con_max:.2f} % menos que el mas lento")
print(f"el super curso de dalto dura un {diferencia_con_prom} % menos que el promedio")
print("-----------------------------------")
#ejercicio B
print(f"un curso promedio elimina el {tiempo_vacio_promedio:.2f}% de tiempo vacio")
print(f"el crack de soydalto elimina un {tiempo_vacio_soydalto:.2f}% de tiempo vacio")
print("-----------------------------------")
#ejercicio C 

print(f"ver 10 horas de soydalto equivalen a {otros_cursos_prom / curso_soydalto * 10:.2f} horas de otros cursos")
print(f"ver 10 horas de otros cursos equivale a ver {curso_soydalto / otros_cursos_prom * 10:.2f} horas del curso soydalto")

