# # In this challenge, you need to calculate and print the sum of elements in an array, considering that some integers may be very large.


# Input Format

# The first line of the input consists of an integer .
# The next line contains n  space-separated integers contained in the array.

# Output Format

# Return the integer sum of the elements in the array.



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.


def aVeryBigSum(ar):
    total = 0
    for element in ar:
        total += element
    return total

if __name__ == '__main__':
    ar_count = int(input("Enter the number of elements: ").strip())
    ar = list(map(int, input(f"Enter {ar_count} space-separated integers: ").strip().split()))

    if len(ar) != ar_count:
        print("Error: Number of integers entered does not match the count.")
    else:
        result = aVeryBigSum(ar)
        print("Sum of the array is:", result)
