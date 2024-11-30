"""
Create a function called generate_random_matrix that takes two arguments: rows and cols. This function should generate a 2D matrix of random integers 
between 1 and 100, with rows rows and cols columns. Use the random module from the Python standard library to generate random numbers.
The matrix should be returned as a list of lists.

Create a function called get_column_sum that takes two arguments: a matrix (2D list) and a column index.
This function should calculate and return the sum of all the values in the specified column of the matrix.

Create a function called get_row_average that takes two arguments: a matrix (2D list) and a row index.
This function should calculate and return the average (mean) of all the values in the specified row of the matrix.
"""

import random

def generate_random_matrix(rows, cols):
    return [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]


def get_column_sum(matrix, column_index):
    if not matrix or column_index < 0 or column_index >= len(matrix[0]):
        raise ValueError("Invalid column index.")
    return sum(row[column_index] for row in matrix)


def get_row_average(matrix, row_index):
    if not matrix or row_index < 0 or row_index >= len(matrix):
        raise ValueError("Invalid row index.")
    return sum(matrix[row_index]) / len(matrix[row_index])


if __name__ == "__main__":
    rows, cols = 5, 4
    matrix = generate_random_matrix(rows, cols)
    print("Generated Matrix:")
    for row in matrix:
        print(row)

    column_index = 2
    column_sum = get_column_sum(matrix, column_index)
    print(f"\nSum of column {column_index}: {column_sum}")

    row_index = 3
    row_avg = get_row_average(matrix, row_index)
    print(f"Average of row {row_index}: {row_avg}")

