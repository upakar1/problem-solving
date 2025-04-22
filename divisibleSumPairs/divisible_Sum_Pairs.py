# ar = [1,2,3,4,5,6]
# k = 5 
# Three pair meets the critaria [1,4][2,3][4,6]
# return number of pairs the meet the condition


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    pair_list = []
    for first_index , first_value in enumerate(ar):
        for second_index , second_value in enumerate(ar):
            if first_index == second_index:
                continue
            if first_index < second_index and (first_value + second_value) % k == 0:
                pair_list.append([first_value , second_value])
    return len(pair_list)

if __name__ == '__main__':
    first_multiple_input = input("Enter n and k: ").rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    ar = list(map(int, input(f"Enter {n} integers: ").rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    print("Number of pairs:", result)

