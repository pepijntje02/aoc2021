import sys, pathlib
parentdir = pathlib.Path(__file__).resolve().parents[1] # Get root direcotry AOC
sys.path.append(str(parentdir))
from myDecorator import time_function

@time_function
def puzzle1(data):
    pass

@time_function
def puzzle2(data):
    pass

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
