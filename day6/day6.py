import sys, pathlib
parentdir = pathlib.Path(__file__).resolve().parents[1] # Get root direcotry AOC
sys.path.append(str(parentdir))
from myDecorator import time_function

from collections import defaultdict

def check_fish(x, data):
    #data is a global variable!
    if x == 0:
        data.append(9)
        return 6
    return x-1

@time_function
def puzzle1(data):
    for _ in range(80):
        data = list(map(lambda x: check_fish(x, data), data))
    return len(data)

@time_function
def puzzle2(data):
    d = defaultdict(int)
    for v in set(data):
        d[v] += data.count(v)
    dold = d
    for _ in range(256):
        dold = d.copy()
        d = defaultdict(int)
        for k, v in dold.items():
            if k == 0:
                d[6] += v
                d[8] += v
            else:
                d[k-1] += v
    return sum(d.values())

if __name__ == '__main__':
    with open('./input.txt') as f:
        data = list(map(int, f.read().rstrip().split(',')))
    # Puzzle 1
    print(f"Puzzle 1: {puzzle1(data)}")
    # Puzzle 2
    print(f"Puzzle 2: {puzzle2(data)}")

'''
Function puzzle1(<class 'list'>,): time elapsed: 647.924 [ms]
Puzzle 1: 360268
Function puzzle2(<class 'list'>,): time elapsed: 1.163 [ms]
Puzzle 2: 1632146183902
'''
