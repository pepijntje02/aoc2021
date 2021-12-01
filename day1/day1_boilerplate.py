import sys, pathlib

parentdir = pathlib.Path(__file__).parents[1] # Get root direcotry AOC
sys.path.append(str(parentdir))
from myDecorator import time_function

@time_function
def puzzle1(data):
    return sum(list(map( lambda x, y: y>x, data[:-1], data[1:])))

@time_function
def puzzle2(data):
    return sum(list(map( lambda x, y: y > x, data[:-3], data[3:])))

@time_function
def puzzle2v2(data):
    return sum([y > x for x,y in zip(data[:-3], data[3:])])

@time_function
def puzzle2v3(data):
    return len([1 for x,y in zip(data[:-3], data[3:]) if y>x])

if __name__ == '__main__':
    with open('./input.txt') as f:
        data = [line.rstrip() for line in f.readlines()]
        try:
            data = list(map(float, data))
        except:
            pass
    # Puzzle 1
    print(f"Puzzle 1: {puzzle1(data)}")
    # Puzzle 2
    print(f"Puzzle 2: {puzzle2(data)}")
    print(f"Puzzle 2: {puzzle2v2(data)}")
    print(f"Puzzle 2: {puzzle2v3(data)}")

'''
Function puzzle1(<class 'list'>,): time elapsed: 0.400 [ms]
Puzzle 1: 1553
Function puzzle2(<class 'list'>,): time elapsed: 0.344 [ms]
Puzzle 2: 1597
Function puzzle2v2(<class 'list'>,): time elapsed: 0.244 [ms]
Puzzle 2: 1597
Function puzzle2v3(<class 'list'>,): time elapsed: 0.123 [ms]
Puzzle 2: 1597
'''
