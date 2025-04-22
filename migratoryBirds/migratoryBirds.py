# Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type. 
# If more than 1 type has been spotted that maximum amount, return the smallest of their ids.

# arr =[1,1,2,2,3]
#  here 1 and 2  occurs 2 time
#  in that case we look at the smallest id


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    no_of_elements = {}
    
    result = []
    

    for value in arr:

        if value in no_of_elements:

            no_of_elements[value] += 1

        else:

            no_of_elements[value] = 1

    max_value = max(no_of_elements.values())

    result = [key for key, value in no_of_elements.items() if value == max_value]
    
    return min(result)


if __name__ == '__main__':
    arr_count = int(input("Enter number of elements: ").strip())
    arr = list(map(int, input("Enter space-separated elements: ").rstrip().split()))
    result = migratoryBirds(arr)
    print("Most frequent bird ID:", result)
