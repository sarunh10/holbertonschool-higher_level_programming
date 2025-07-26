#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div and returns a new matrix."""
    
    # Check that matrix is a list of lists with int/float elements
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check each element in each row is int or float
    for row in matrix:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check all rows are of the same size
    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    # Check div is a number and not zero
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Return new matrix with elements divided and rounded
    return [[round(num / div, 2) for num in row] for row in matrix]

