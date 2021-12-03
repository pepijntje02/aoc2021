import sys, pathlib
parentdir = pathlib.Path(__file__).parents[1] # Get root direcotry AOC
sys.path.append(str(parentdir))
from myDecorator import time_function

@time_function
def puzzle1(data):
    # Data is NxM array with integers
    # Transform array
    d = list(zip(*data))
    # Go over each bit and determine most common bit
    gamma = [1 if len(ele)/2 < sum(ele) else 0 for ele in d ]
    # Use XOR to get opposite of gamma
    epsilon = [ele^1 for ele in gamma]
    # Transform to string
    gamma = ''.join(map(str,gamma))
    epsilon = ''.join(map(str,epsilon))
    return int(gamma, base=2) * int(epsilon, base=2)

@time_function
def puzzle2(data):
    # Recursive function which manipulates list (does not return list) 
    def search_numbers(array, index, type=None):
        # get column based on index
        temp = list(zip(*array))[index]
        # Get current number with most occurrences at index
        number = int( len(temp) / 2 <= sum(temp) )
        # Xor if type is co2
        if type == 'co2':
            number = number^1
        # Pop elements if number is not equal to given number
        for i in range(len(array)-1, -1, -1):
            if array[i][index] != number:
                array.pop(i)
        if len(array) > 1:
            search_numbers(array, index+1, type=type)
    
    # copy list
    oxygen = data.copy()
    co2 = data.copy()
    search_numbers(oxygen, 0)
    search_numbers(co2, 0, 'co2')

    oxygen = ''.join(map(str, oxygen[0]))
    co2 = ''.join(map(str, co2[0]))
    return int(oxygen, 2) * int(co2, 2)

if __name__ == '__main__':
    with open('./input.txt') as f:
        data = [list(map(int,line.rstrip())) for line in f.readlines()]
    # Puzzle 1
    print(f"Puzzle 1: {puzzle1(data)}")
    # Puzzle 2
    data = [list(map(int, ele)) for ele in data]
    print(f"Puzzle 2: {puzzle2(data)}")

'''
Function puzzle1(<class 'list'>,): time elapsed: 0.288 [ms]
Puzzle 1: 2648450
Function puzzle2(<class 'list'>,): time elapsed: 0.979 [ms]
Puzzle 2: 2845944
'''