# Funciones de multiplicación de matrices
def matrix_multiply_traditional(A, B):
    n = len(A)  # Asumiendo matrices cuadradas
    C = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def matrix_multiply_optimized(A, B):
    n = len(A)  # Asumiendo matrices cuadradas
    C = [[0] * n for _ in range(n)]

    # Transponer la matriz B
    B_T = [[B[j][i] for j in range(n)] for i in range(n)]

    # Realizar la multiplicación de matrices con B transpuesta
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B_T[j][k]
    return C

def matrix_add(A, B):
    n = len(A)  # Asumiendo matrices cuadradas
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def matrix_subtract(A, B):
    n = len(A)  # Asumiendo matrices cuadradas
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

def matrix_multiply_strassen(A, B):
    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2

    # Dividir las matrices en submatrices
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    # Calcular los productos de Strassen
    M1 = matrix_multiply_strassen(matrix_add(A11, A22), matrix_add(B11, B22))
    M2 = matrix_multiply_strassen(matrix_add(A21, A22), B11)
    M3 = matrix_multiply_strassen(A11, matrix_subtract(B12, B22))
    M4 = matrix_multiply_strassen(A22, matrix_subtract(B21, B11))
    M5 = matrix_multiply_strassen(matrix_add(A11, A12), B22)
    M6 = matrix_multiply_strassen(matrix_subtract(A21, A11), matrix_add(B11, B12))
    M7 = matrix_multiply_strassen(matrix_subtract(A12, A22), matrix_add(B21, B22))

    # Combinar las submatrices para formar la matriz resultante
    C11 = matrix_add(matrix_subtract(matrix_add(M1, M4), M5), M7)
    C12 = matrix_add(M3, M5)
    C21 = matrix_add(M2, M4)
    C22 = matrix_add(matrix_subtract(matrix_add(M1, M3), M2), M6)

    # Crear la matriz resultante a partir de las submatrices
    C = [[0] * n for _ in range(n)]
    for i in range(mid):
        C[i][:mid] = C11[i]
        C[i][mid:] = C12[i]
        C[mid + i][:mid] = C21[i]
        C[mid + i][mid:] = C22[i]

    return C