def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions")

    result_matrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result_matrix.append(row)

    return result_matrix

def transpose_matrix(matrix):
    transposed_matrix = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        transposed_matrix.append(row)

    return transposed_matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
result_matrix = add_matrices(matrix1, matrix2)
transposed_matrix = transpose_matrix(result_matrix)
print("Matrix 1:")
print_matrix(matrix1)

print("\nMatrix 2:")
print_matrix(matrix2)

print("\nResult Matrix:")
print_matrix(result_matrix)

print("\nTransposed Matrix:")
print_matrix(transposed_matrix)
