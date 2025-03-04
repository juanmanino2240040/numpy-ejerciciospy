import numpy as np

# Se definen numero de candidatos y total de votos
num_candidatos = 30
total_votos = 5000

# Con el random.multinomial se generan 30 numeros aleatorios que suman que sumados dan 5000. Estos 30 numeros se guardan en la variable votos_por_candidato. El primer parámetro es lo que da la suma total y el segundo parámetro es la probabilidad para cada uno de los 30 valores, 0.1.
votos_por_candidato = np.random.multinomial(total_votos, np.ones(num_candidatos) / num_candidatos)

# Un array de los candidatos del 1 al 30
candidatos = np.arange(1, num_candidatos + 1)

# Se ordenan los candidatos en orden ascendente. argsort devuelve los indices de los elementos ordenados, es decir, toma el valor de votos mas alto y devuelve ese indice primerl, luego el del segundo mas alto, etc.
indices_ordenados = np.argsort(-votos_por_candidato)  # El negativo invierte el orden a descendente, por ejemplo, pasa de 1-2-3...a 30-29-28...
candidatos_ordenados = candidatos[indices_ordenados]  # Reordenar candidatos
votos_ordenados = votos_por_candidato[indices_ordenados]  # Reordenar votos
# Candidatos y votos ordenados reorganiza los dos array para que esten en el orden descendente de votos con su respectivo numero de candidato y cantidad de votos

# Imprimir. Se usa for each para recorrer los array, y el zip forma parejas ordenadas entre los dos array recorridos. En los array ordenados, se crean nuevos indices con el orden descendente
print("\nVotos por candidato: no ordenados):")
for candidate, votes in zip(candidatos, votos_por_candidato):
    print(f"Candidate {candidate} received {votes} votes")

print("\nVotos por candidato: orden descendente):")
for candidate, votes in zip(candidatos_ordenados, votos_ordenados):
    print(f"Candidate {candidate} received {votes} votes")