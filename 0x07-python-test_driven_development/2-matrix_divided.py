#!/usr/bin/env python3
""" This module is a function that divides all elements of a matrix."""

def matrix_divided(matrix, div):
    """
    This function divides all elements of a matrix

    @matrix: a list of integers or floats
    @div: a number (integer or float)

    The function returns a new matrix
    """
    if (not isinstance(matrix, list)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if (len(matrix) < 1):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if (not isinstance(row, list)):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        for element in row:
            if (not isinstance(element, (int, float))):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    length = len(matrix[0])
    for row in matrix:
        if(len(row) != length):
            raise TypeError("Each row of the matrix must have the same size")
    if (not isinstance(div, int) and not isinstance(div, float)):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
