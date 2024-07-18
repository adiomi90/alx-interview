#!/usr/bin/python3
""" Rotate 2D Matrix """

def rotate_2d_matrix(matrix):
    """
    Rotates a given 2D matrix in-place by 90 degrees clockwise.

    Args:
        matrix (list[list]): The 2D matrix to be rotated.

    Returns:
        None: The function modifies the matrix in-place.

    Example:
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        rotate_2d_matrix(matrix)
        print(matrix)
        # Output: [[7, 4, 1],
        #          [8, 5, 2],
        #          [9, 6, 3]]
    """
   
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp

    for i in range(n):
        for j in range(int(n / 2)):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[i][n-1-j]
            matrix[i][n-1-j] = tmp
