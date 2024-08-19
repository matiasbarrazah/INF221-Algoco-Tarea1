import time
import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Importar funciones de los archivos existentes
from Sortingalg import selection_sort, pysort, quicksort, mergesort
from Matrixmult import matrix_multiply_traditional, matrix_multiply_optimized, matrix_multiply_strassen

# Cargar los datasets de listas
with open('ArrayDatasets/almost_sorted_list.json', 'r') as f:
    almost_sorted_list = json.load(f)
with open('ArrayDatasets/random_list.json', 'r') as f:
    random_list = json.load(f)
with open('ArrayDatasets/reverse_sorted_list.json', 'r') as f:
    reverse_sorted_list = json.load(f)
with open('ArrayDatasets/sorted_list.json', 'r') as f:
    sorted_list = json.load(f)
with open('ArrayDatasets/partially_sorted_list.json', 'r') as f:
    partially_sorted_list = json.load(f)

# Cargar los datasets de matrices cuadradas
with open('MatrixDatasets/square_matrix.json', 'r') as f:
    square_matrix = json.load(f)
with open('MatrixDatasets/sparse_matrix.json', 'r') as f:
    sparse_matrix = json.load(f)
with open('MatrixDatasets/identity_matrix.json', 'r') as f:
    identity_matrix = json.load(f)
with open('MatrixDatasets/diagonal_matrix.json', 'r') as f:
    diagonal_matrix = json.load(f)

# Definir los datasets de matrices en un diccionario
matrix_datasets = {
    "Square Matrix 128x128": square_matrix,
    "Sparse Matrix 128x128": sparse_matrix,
    "Identity Matrix 128x128": identity_matrix,
    "Diagonal Matrix 128x128": diagonal_matrix
}

# Función para medir tiempo de ejecución
def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return end_time - start_time, result

# Ejecutar pruebas de ordenamiento
sorting_algorithms = {
    "Selection Sort": selection_sort,
    "Python Sort (Timsort)": pysort,
    "Quicksort": quicksort,
    "Mergesort": mergesort
}

list_datasets = {
    "Almost Sorted List": almost_sorted_list,
    "Random List": random_list,
    "Reverse Sorted List": reverse_sorted_list,
    "Sorted List": sorted_list,
    "Partially Sorted List": partially_sorted_list
}

sorting_results = {}
for algo_name, algo_func in sorting_algorithms.items():
    sorting_results[algo_name] = []
    for dataset_name, dataset in list_datasets.items():
        exec_time, _ = measure_time(algo_func, dataset.copy())
        sorting_results[algo_name].append(exec_time)

# Crear gráficos para los algoritmos de ordenamiento
fig, ax = plt.subplots()
index = np.arange(len(list_datasets))
bar_width = 0.2

for i, (algo_name, times) in enumerate(sorting_results.items()):
    ax.bar(index + i * bar_width, times, bar_width, label=algo_name)

ax.set_xlabel('Datasets')
ax.set_ylabel('Tiempo de ejecución (s)')
ax.set_title('Comparación de Algoritmos de Ordenamiento')
ax.set_xticks(index + bar_width)
ax.set_xticklabels(list_datasets.keys(), rotation=45, ha="right")
ax.legend()

plt.tight_layout()
plt.show()

# Ejecutar pruebas de multiplicación de matrices
matrix_algorithms = {
    "Traditional Multiplication": matrix_multiply_traditional,
    "Optimized Multiplication": matrix_multiply_optimized,
    "Strassen Multiplication": matrix_multiply_strassen
}

matrix_results = {}
for algo_name, algo_func in matrix_algorithms.items():
    matrix_results[algo_name] = []
    for dataset_name, dataset in matrix_datasets.items():
        exec_time, result = measure_time(algo_func, dataset, dataset)
        matrix_results[algo_name].append(exec_time if result is not None else np.nan)

# Crear gráficos para los algoritmos de multiplicación de matrices
fig, ax = plt.subplots()
index = np.arange(len(matrix_datasets))
bar_width = 0.2

for i, (algo_name, times) in enumerate(matrix_results.items()):
    # Usar np.nan para los valores faltantes
    valid_times = np.array(times)
    ax.bar(index + i * bar_width, valid_times, bar_width, label=algo_name)

ax.set_xlabel('Datasets')
ax.set_ylabel('Tiempo de ejecución (s)')
ax.set_title('Comparación de Algoritmos de Multiplicación de Matrices')
ax.set_xticks(index + bar_width)
ax.set_xticklabels(matrix_datasets.keys(), rotation=45, ha="right")
ax.legend()

plt.tight_layout()
plt.show()

# Crear tablas de resultados
# Resultados de ordenamiento
sorting_df = pd.DataFrame(sorting_results, index=list_datasets.keys())
print("\nResultados de Ordenamiento:\n", sorting_df)

# Resultados de multiplicación de matrices
matrix_df = pd.DataFrame(matrix_results, index=matrix_datasets.keys())
print("\nResultados de Multiplicación de Matrices:\n", matrix_df)

# Guardar resultados en archivos CSV
sorting_df.to_csv('sorting_results.csv')
matrix_df.to_csv('matrix_results_128.csv')