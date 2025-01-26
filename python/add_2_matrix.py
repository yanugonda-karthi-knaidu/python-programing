#write a python program yp add, transpose and multiply two matrices
def add_matrices(matrix_a, matrix_b):
    if len(matrix_a) == len(matrix_b) and len(matrix_a[0]) == len(matrix_b[0]):
        result = [[matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]
        return result
    else:
        raise ValueError("Matrices must have the same dimensions for addition.")
    
def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def multiply_matrices(matrix_a, matrix_b):
    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")
    
    result = [[0 for _ in range(len(matrix_b[0]))] for _ in range(len(matrix_a))]
    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            for k in range(len(matrix_b)):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result
def main():
    matrix_a = [ 
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    matrix_b = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]

    try:
        sum_result = add_matrices(matrix_a, matrix_b)
        print("Sum of matrices:")
        for row in sum_result:
            print(row)
    except ValueError as e:
        print(e)

    transposed_a = transpose_matrix(matrix_a)
    print("\nTransposed Matrix A:")
    for row in transposed_a:
        print(row)

    try:
        product_result = multiply_matrices(matrix_a, matrix_b)
        print("\nProduct of matrices:")
        for row in product_result:
            print(row)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()