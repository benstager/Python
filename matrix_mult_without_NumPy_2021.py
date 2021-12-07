## This is an algorithm I attempted to write to multiply two square matrices

## NumPy can make matrix multiplciation a lot easier, but I wanted to try to write
## an algorithm that does it manually

## matrixA must be n X n and matrix B must be n X n, where n can be any number

## The function takes in matrixA and matrix B
## matrix[i][j] is the ith row and jth element of either matrix

## The algorithm iterates through each row of A and each column of B, multiplying
## The elements of row i of A by the elements of column i of B
## matrix_res is of size [n][n] 

## The matrices are printed using correct formatting as well

def matrix_multiply(matrixA, matrixB):
    matrix_res = [[0,0,0],[0,0,0],[0,0,0]]


    for i in range(len(matrixA)):
        for j in range(len(matrixB[0])):
            for k in range(len(matrixB)):
                matrix_res[i][j] += matrixA[i][k] * matrixB[k][j]

    for x in range(len(matrix_res)):
        print(matrix_res[x])
            
        





matrix1 = [[1,2,3],[3,2,1],[1,1,0]]
matrix2 = [[7,3,2],[1,1,2],[4,2,1]]


matrix_multiply(matrix1,matrix2)
