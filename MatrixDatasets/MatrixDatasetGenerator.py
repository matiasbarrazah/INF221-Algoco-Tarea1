import numpy as np
import json

def generate_square_matrix(n, low=1, high=100):
    """Genera una matriz cuadrada nxn con valores aleatorios."""
    return np.random.randint(low, high, size=(n, n))

def generate_sparse_matrix(n, sparsity=0.9, low=1, high=100):
    """Genera una matriz cuadrada nxn esparcida con una fracción dada de ceros."""
    matrix = np.random.randint(low, high, size=(n, n))
    mask = np.random.rand(n, n) < sparsity
    matrix[mask] = 0
    return matrix

def generate_identity_matrix(n):
    """Genera una matriz identidad nxn."""
    return np.eye(n)

def generate_diagonal_matrix(n, low=1, high=100):
    """Genera una matriz diagonal nxn con valores aleatorios en la diagonal."""
    diagonal_values = np.random.randint(low, high, size=n)
    return np.diag(diagonal_values)

# Generar matrices cuadradas de 128x128
size = 128

with open('square_matrix.json', 'w') as f:
    json.dump(generate_square_matrix(size).tolist(), f)

with open('sparse_matrix.json', 'w') as f:
    json.dump(generate_sparse_matrix(size, sparsity=0.95).tolist(), f)

with open('identity_matrix.json', 'w') as f:
    json.dump(generate_identity_matrix(size).tolist(), f)

with open('diagonal_matrix.json', 'w') as f:
    json.dump(generate_diagonal_matrix(size).tolist(), f)
