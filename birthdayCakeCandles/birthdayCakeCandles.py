# You are in charge of the cake for a child's birthday. It will have one candle for each year of their total age.
#  They will only be able to blow out the tallest of the candles. Your task is to count how many candles are the tallest.

#  candles = [4,4,1,3]
#  The tallest candles are 4 units high. There are 2 candles with this height, so the function should return 2.



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#




def birthdayCakeCandles(candles):
    tallest = max(candles)
    count = 0
    for candle in candles:
        if candle == tallest:
            count += 1
    return count

if __name__ == '__main__':
    candles_count = int(input("Enter number of candles: ").strip())

    candles = list(map(int, input(f"Enter {candles_count} candle heights: ").rstrip().split()))

    result = birthdayCakeCandles(candles)

    print("Number of tallest candles:", result)
