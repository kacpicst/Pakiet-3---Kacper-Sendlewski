def transpose_matrix(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

original_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = transpose_matrix(original_matrix)
print(result)