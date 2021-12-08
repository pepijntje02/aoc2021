from functools import lru_cache
import sys, pathlib
DIR = pathlib.Path(__file__).parent
parentdir = DIR.resolve().parent # Get root direcotry AOC
sys.path.append(str(parentdir))
from myDecorator import time_function

import numpy as np
from functools import lru_cache

@time_function
def puzzle1(data):
    # Find minimum in data:
    data = np.array(data)
    s = 1e9
    for t in range(min(data), max(data)):
        sold, s = s, np.sum(np.abs(data - t))
        if s > sold:
            break
    t -= 1
    return np.sum(np.abs(data-t))

@lru_cache(maxsize=None)
def iter_sum(x):
    return x * (x+1) /2

@time_function
def puzzle2(data):
    data = np.array(data)
    s = 1e9
    # m1 = int(np.mean(data))
    for t in range(min(data), max(data)):
        sold, s = s, np.sum(list(map(iter_sum, np.abs(data - t))))
        if s > sold:
            break
    t -= 1
    return np.sum(list(map(iter_sum,np.abs(data-t))))

if __name__ == '__main__':
    with open('input.txt') as f:
        data = list(map(int, f.read().split(',')))
    # Puzzle 1
    print(f"Puzzle 1: {puzzle1(data)}")
    # Puzzle 2
    print(f"Puzzle 2: {puzzle2(data)}")

'''
Function puzzle1(<class 'list'>,): time elapsed: 2.467 [ms]
Puzzle 1: 328262
Function puzzle2(<class 'list'>,): time elapsed: 98.504 [ms]
Puzzle 2: 90040997
'''