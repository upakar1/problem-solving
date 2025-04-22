# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four
# of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated
# long integers.

# arr= [1,3,5,7,9]
# minimum sum = (1+3+5+7)
# maximum_sum = (3+5+7+9)



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    total_sum = sum(arr)
    min_sum = total_sum - max(arr)
    max_sum = total_sum - min(arr)
    print(min_sum, max_sum)

if __name__ == '__main__':
    arr = list(map(int, input("Enter 5 space-separated integers: ").rstrip().split()))
    
    if len(arr) != 5:
        print("Error: Please enter exactly 5 integers.")
    else:
        miniMaxSum(arr)
