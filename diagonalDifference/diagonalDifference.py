# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# For example, the square matrix  is shown below:

# 1 2 3
# 4 5 6
# 9 8 9

# The left-to-right diagonal =1+5+6 = 15 .
# The right-to-left diagonal = 3+5+9 = 17
# Their absolute difference is |15-17| = 2




#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#



def diagonalDifference(arr):
    left_to_right_diagonal = 0
    right_to_left_diagonal = 0

    length_of_array = len(arr)

    for i in range(length_of_array):
        left_to_right_diagonal += arr[i][i]
        right_to_left_diagonal += arr[i][length_of_array - 1 - i]

    differences = abs(left_to_right_diagonal - right_to_left_diagonal)
    return differences


if __name__ == '__main__':
    n = int(input("Enter size of square matrix: ").strip())

    arr = []
    print(f"Enter the {n} rows of the matrix (space-separated):")
    for _ in range(n):
        row = list(map(int, input().rstrip().split()))
        if len(row) != n:
            print("Error: Each row must have exactly", n, "elements.")
            exit()
        arr.append(row)

    result = diagonalDifference(arr)

    print("Absolute difference between diagonals:", result)
