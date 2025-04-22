# Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.

# The rating for Alice's challenge is the triplet a = (a[0], a[1], a[2]), and the rating for Bob's challenge is the triplet b = (b[0], b[1], b[2]).

# The task is to calculate their comparison points by comparing each category:

# If a[i] > b[i], then Alice is awarded 1 point.
# If a[i] < b[i], then Bob is awarded 1 point.
# If a[i] = b[i], then neither person receives a point.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b



def compareTriplets(a, b):
    alice = 0
    bob = 0
    for i in range(3):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
    return (alice, bob)

if __name__ == '__main__':
    a = list(map(int, input("Enter Alice's ratings (3 integers): ").rstrip().split()))
    b = list(map(int, input("Enter Bob's ratings (3 integers): ").rstrip().split()))

    if len(a) != 3 or len(b) != 3:
        print("Error: Please enter exactly 3 ratings for both Alice and Bob.")
    else:
        result = compareTriplets(a, b)
        print("Comparison Points -> Alice:", result[0], "Bob:", result[1])
