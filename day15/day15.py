import sys, pathlib
DIR = pathlib.Path(__file__).parent
parentdir = DIR.resolve().parent # Get root direcotry AOC
sys.path.append(str(parentdir))
from myDecorator import time_function

from collections import defaultdict, deque

def change_dict_value(d, cost, positions):
    # d: data (i,j) with value
    # cost: cost dict for (i,j) 
    # position: current postion
    changed = False
    for position in positions:
        i,j = position
        surround = set([(i-1,j), (i+1,j), (i,j-1), (i,j+1)]) & set(positions)
        for pos in surround:
            value = cost[position] + d[pos]
            if  cost[pos] > value or cost[pos] < 0:
                cost[pos] = value
                changed = True
    return changed, cost

@time_function
def puzzle1(data):
    width, height = len(data[0]), len(data)
    d = {(i,j): data[j][i] for j in range(height) for i in range(width)}
    positions = list(d.keys())
    cost = defaultdict(lambda: -1)
    cost[(0,0)] = d[(0,0)]
    START = (0,0)
    # change_dict_value(d, cost, START, set(d.keys()))
    changed = True
    while changed:
        changed, cost = change_dict_value(d, cost, positions)
    return cost[(width-1, height-1)] - d[(0,0)]

def change_dict_value_v2(d, width, height):
    #keep track where you are:
    coords = [(0,0)]
    coords = deque([(0,0)])
    risk = {(0,0):d[(0,0)]}
    positions = set(d.keys())

    while len(coords) > 0:
        i,j = coords.pop()
        v = risk.get((i,j), 0)
        neighbours = set([(i-1,j), (i+1,j), (i,j-1), (i,j+1)]) & positions
        for neighbour in neighbours:
            neighbour_value = d[neighbour] + v
            if neighbour not in risk or  neighbour_value < risk.get(neighbour, -1):
                risk[neighbour] = neighbour_value
                # insert instead of append!!
                # coords.insert(0, neighbour)
                coords.appendleft(neighbour)
    return risk

def change_dict_value_v2_priority(d, width, height):
    '''' 
    Try with priority queue and stop when (49,49) is reached.
    '''
    # from heapq import heappush, heappop
    from queue import PriorityQueue
    q = PriorityQueue()
    q.put((d[(0,0)], (0,0)))
    risk = {(0,0):d[(0,0)]}
    positions = set(d.keys())
    while not q.empty():
        v, (i,j) = q.get()
        neighbours = set([(i-1,j), (i+1,j), (i,j-1), (i,j+1)]) & positions
        for neighbour in neighbours:
            neighbour_value = d[neighbour] + v
            if neighbour not in risk or  neighbour_value < risk[neighbour]:
                risk[neighbour] = neighbour_value
                if neighbour == (width-1, height-1):
                    return risk
                q.put((neighbour_value, (neighbour)))
    return risk

def create_grid(data, n=5):
    width, height = len(data[0]), len(data)
    d = {(i,j): (data[j%height][i%width] + i//width + j//width - 1)%9 + 1  \
             for j in range(height * n) for i in range(width*n)}
    return d, width * n, height * n

def check_grid(grid, width, height):
    import numpy as np
    g = np.zeros((width, height))
    for key, value in grid.items():
        g[key[0], key[1]] = value
    return g.T

@time_function
def puzzle2(data, part=2):
    if part == 2:
        d, width, height = create_grid(data)
    else:
        width, height = len(data[0]), len(data)
        d = {(i,j): data[j][i] for j in range(height) for i in range(width)}
    # risk = change_dict_value_v2(d, width, height)
    risk = change_dict_value_v2_priority(d, width, height)
    return risk[(width-1, height-1)] - d[(0,0)]

if __name__ == '__main__':
    with open(DIR / 'input.txt') as f:
        data = [list(map(int, line.rstrip())) for line in f.readlines()]
    # Puzzle 1
    # print(f"Puzzle 1: {puzzle1(data)}") # too slow (one minute on part 1)
    print(f"Puzzle 1: {puzzle2(data, part=1)}")
    # Puzzle 2
    print(f"Puzzle 2: {puzzle2(data)}")

'''
Function puzzle1(<class 'list'>,): time elapsed: 61068.447 [ms]
Puzzle 1: 447
Function puzzle2(<class 'list'>, "part=<class 'int'>"): time elapsed: 90.294 [ms]
Puzzle 1: 447
Function puzzle2(<class 'list'>,): time elapsed: 9174.151 [ms]
Puzzle 2: 2825

with priorityqueue:
Function puzzle2(<class 'list'>, "part=<class 'int'>"): time elapsed: 62.954 [ms]
Puzzle 1: 447
Function puzzle2(<class 'list'>,): time elapsed: 1799.874 [ms]
Puzzle 2: 2825
'''