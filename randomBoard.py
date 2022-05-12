import random

length = 10
width = 10

array = [[random.randint(0, 9) for i in range(length)] for j in range(width)]


def print2DArray(array):
    for i in range(0, len(array)):
        print (array[i])

print2DArray(array)  

def findSum(array):
    sum = 0
    for i in range(0, len(array)):
        for j in range (0, len(array)):
            sum += array[i][j]
    print(sum)


findSum(array)