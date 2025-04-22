arr = [1,1,0,-1,-1]
def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    for element in arr:
        if element > 0 :
            positive += 1
        elif element < 0 :
            negative += 1
        else:
            zero += 1
    return positive , negative , zero

pos , neg , zer = plusMinus(arr)
length_of_the_list = len(arr)
print(f"{pos / length_of_the_list:6f}")
print(f"{neg / length_of_the_list:6f}")
print(f"{zer/ length_of_the_list:6f}")




