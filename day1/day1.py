import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from myDecorator import time_function

with open('./input.txt') as f:
    data = [float(line) for line in f.readlines()]

def increase(data):
    f = lambda x, y: y > x
    return sum( list(map(f, data[:-1], data[1:])) )

@time_function
def puzzle1(data):
    return increase(data)

print(f"Puzzle 1: {puzzle1(data)}")

def sliding_window(array):
    return [sum(array[i:i+3]) for i in range(len(array)-2)]

@time_function
def puzzle2(data):
    three_sum = sliding_window(data)
    return increase(three_sum) 

print(f"Puzzle 2: {puzzle2(data)}")

# And now with thinking, i.e. use math instead of brute force
# If the list is: a, b, c, d then the moving difference is:
# (b + c + d) - (a + b + c) = d - a i.e. index 0 and index 2.
# Rewrite increase function:

def increasev2(data, step):
    f = lambda x, y: y > x
    return sum( list(map(f, data[:-step], data[step:])) )

@time_function
def puzzle2v2(data):
    return increasev2(data, step=3)

print(f"Puzzle 2: {puzzle2v2(data)}")

'''
Function puzzle1(*args, **kwargs): time elapsed: 0.218 [ms]
Puzzle 1: 1553
Function puzzle2(*args, **kwargs): time elapsed: 0.657 [ms]
Puzzle 2: 1597
Function puzzle2v2(*args, **kwargs): time elapsed: 0.199 [ms]
Puzzle 2: 1597
'''