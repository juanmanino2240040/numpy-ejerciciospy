import numpy as np

# Se define numero de total de estudiantes

num_estudiantes=6500
#Con random.randint se crean valores aleatorios con el primer parametro como limite inferior incluyente y el segundo como limite superior excluyente. Se crean tantos valores como sea el size.
# El codigo de estudiante lo conformé como primeros cuatro digitos, el año, siguientes dos, codigo de carrera de 10 a 45 y ultimos dos, numeros al azar entro 0 y 99. Por ejemplo: 1987-31-08
year_est=np.random.randint(1975, 2026, size=num_estudiantes)
carrera_est=np.random.randint(10, 46, size=num_estudiantes)
final_est=np.random.randint(1, 100, size=num_estudiantes)

# El nombre consiste en la palabra "Estudiante_" y un numero interado tantas veces como estudiantes haya
nombres=np.array(["Estudiante_" + str(i) for i in range(num_estudiantes)])
#El codigo se conforma de combinar los tres valores random definidios con antelación
codigo_est=(year_est*10000)+(carrera_est*100)+final_est

# Para el promedio, round redondea los numeros del array a 2 decimales, y el random.uniform genera numeros uniformemente distribuidos en los numeros y acatados al size
prom= np.round(np.random.uniform(0.0, 5.0, size=num_estudiantes), 2)

# ------------------------- Filtro de CARRERA X -------------------------
carrera_x = int(input("Ingrese el còdigo de la carrera (10-50): "))  # Input de usuario

# Tomar los estudiantes de la carrera X con prom >= 4.0
filtro_carrera_x = (carrera_est == carrera_x) & (prom >= 4.0) # Se crea el filtro para los array
cods_filtros_prom = codigo_est[filtro_carrera_x] # Se pasa el filtro como parametro para los array y los valores que cumplan la condicion, prom>=4.0, se quedan en cods_filtro.
nombres_filtrados_prom = nombres[filtro_carrera_x]

# El filtro crea un array booleanode True y False si se cumple la condicion. Como todos los array se relacionan por su indice de posición, es decir, el indice 0 de year_est corresponde al indice 0 del carrera_est,final_est, nombres, prom y codigo, entonces al pasarles el filtro se guardaran solo los valores del array que corresponden a los estudiantes correctos
                            
print("\nEstudiantes en la carrera ", carrera_x, "con Promedio >= 4.0:")
for code, name in zip(cods_filtros_prom, nombres_filtrados_prom):
    print(f"Codigo: {code}, Nombre: {name}")

print("Total  de estudiantes en la carrera ", carrera_x, "con promedio >= 4.0:", len(cods_filtros_prom))


input("Presione cualquier tecla para continuar ") # Pausa para ver los valores de carrera X. Si se corre todo el codigo junto, todos los datos del filtro por año no dejan ver los de carrera x.,

# ------------------------- FILTRO POR AÑO <1990 -------------------------

# Tomar los estudiantes con año de ingreso menor a 1990. Se usa la misma lógica del promedio y se filtran los array
filtro_condicional = (year_est <1990) & (prom < 3.0)
cods_filtros = codigo_est[filtro_condicional]
nombres_filtrados = nombres[filtro_condicional]
                            
print("\n Estudiantes que entraron antes de 1990 y estan condicionales (Prom < 3.0):  ")
for code, name in zip(cods_filtros, nombres_filtrados):
    print(f"Code: {code}, Name: {name}")

print("Total de estudiantes que entraron antes de 1990 y estan condicionales:", len(cods_filtros))