# Write a twoDlist function that perform 3×3 matrix multiplication.
def twoDlist(matrix1, matrix2):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    for i in range(3):  
        for j in range(3):  
            for k in range(3):  
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result_matrix = twoDlist(matrix1, matrix2)

for row in result_matrix:
    print(row)
