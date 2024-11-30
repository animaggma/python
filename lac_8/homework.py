"""
Create a Matrix class that accepts n and m variables as the number of rows and columns,
generates a matrix in the constructor, and supports the following operations(each point should be separate function):
Prints a matrix.
Calculate the mean of the matrix.
Calculate the sum of a given row.
Calculate the average of a given column.
function that accepts [col1, col2, row1, row2] and prints a submatrix.
"""
import random

class Matrix:
    def __init__(self, n, m):
        self.rows = n
        self.cols = m
        self.matrix = [[random.randint(1, 100) for _ in range(m)] for _ in range(n)]

    def print_matrix(self):
        print("Matrix:")
        for row in self.matrix:
            print(row)

    def calculate_mean(self):
        total_sum = sum(sum(row) for row in self.matrix)
        total_elements = self.rows * self.cols
        return total_sum / total_elements

    def row_sum(self, row_index):
        if row_index < 0 or row_index >= self.rows:
            raise ValueError("Invalid row index.")
        return sum(self.matrix[row_index])

    def column_average(self, col_index):
        if col_index < 0 or col_index >= self.cols:
            raise ValueError("Invalid column index.")
        return sum(row[col_index] for row in self.matrix) / self.rows

    def print_submatrix(self, col1, col2, row1, row2):
        if not (0 <= col1 < self.cols and 0 <= col2 < self.cols and
                0 <= row1 < self.rows and 0 <= row2 < self.rows):
            raise ValueError("Invalid submatrix indices.")
        print("Submatrix:")
        for row in self.matrix[row1:row2+1]:
            print(row[col1:col2+1])


if __name__ == "__main__":
    n, m = 5, 4
    my_matrix = Matrix(n, m)
    my_matrix.print_matrix()
    print(f"\nMean of the matrix: {my_matrix.calculate_mean()}")
    row_index = 2
    print(f"Sum of row {row_index}: {my_matrix.row_sum(row_index)}")
    col_index = 1
    print(f"Average of column {col_index}: {my_matrix.column_average(col_index)}")
    col1, col2, row1, row2 = 1, 3, 1, 3
    my_matrix.print_submatrix(col1, col2, row1, row2)
