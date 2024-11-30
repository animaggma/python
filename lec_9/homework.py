"""
Create a Matrix class that accepts the number of rows and columns as parameters in the constructor.
Generate a matrix directly in the constructor.
Implement the __str__ method for the Matrix class. Additionally, 
implement the mathematical operations for addition (+), subtraction (-), and multiplication (*) for the Matrix class.
"""

import random

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        matrix_str = "\n".join(["\t".join(map(str, row)) for row in self.matrix])
        return matrix_str

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition.")
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(self.rows, self.cols, result)

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for subtraction.")
        result = [[self.matrix[i][j] - other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(self.rows, self.cols, result)

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrices must have compatible dimensions for multiplication.")
        result = [[sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.cols)) for j in range(other.cols)] for i in range(self.rows)]
        return Matrix(self.rows, other.cols, result)

    def __init__(self, rows, cols, matrix=None):
        self.rows = rows
        self.cols = cols
        self.matrix = matrix if matrix is not None else [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]

if __name__ == "__main__":
    matrix1 = Matrix(3, 3)
    matrix2 = Matrix(3, 3)
    
    print("Matrix 1:")
    print(matrix1)
    
    print("\nMatrix 2:")
    print(matrix2)
    
    matrix_sum = matrix1 + matrix2
    print("\nMatrix 1 + Matrix 2:")
    print(matrix_sum)
    
    matrix_diff = matrix1 - matrix2
    print("\nMatrix 1 - Matrix 2:")
    print(matrix_diff)
    
    matrix_prod = matrix1 * matrix2
    print("\nMatrix 1 * Matrix 2:")
    print(matrix_prod)
