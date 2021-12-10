import sys, pathlib
DIR = pathlib.Path(__file__).parent
parentdir = DIR.resolve().parent # Get root direcotry AOC
sys.path.append(str(parentdir))
from myDecorator import time_function

from functools import reduce

def check_depth(i, j, depth):
    d = depth[(i,j)]
    # surrounding above, left, under, right:
    coords = [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]
    local_minimum = sum([d < depth.get(x, 10) for x in coords]) == 4
    return local_minimum, coords

@time_function
def puzzle1(data):
    M = len(data)
    N = len(data[0])
    l = [list(zip([x] * N, range(N))) for x in range(M)]
    l = reduce(lambda x,y : x+y, l)
    data = reduce(lambda x,y : x+y, data)
    # Depthmap:
    depth = dict(zip(l, data))
    check_coordinates = l.copy()
    local = {}
    for i in range(M):
        for j in range(N):
            # Check if value should be checktaed AND check if it is minimum.
            if (i,j) in check_coordinates:
                local_min, coords =  check_depth(i, j, depth)
                if local_min:
                    local[(i,j)] = depth[(i,j)]
                    for coord in coords:
                        try:
                            check_coordinates.remove(coord)
                        except:
                            pass
                else:
                    check_coordinates.remove((i,j))
    return sum(local.values()) + len(local)

def check_in_existing_basin(i, j, basins):
    coords = set([(i-1, j), (i, j-1), (i+1, j), (i, j+1)])
    append = False
    for basin in basins:
        if coords & set(basin):
            if append == False:
                basin.append((i,j))
                append = basin
            else:
                append += basin
                basins.remove(basin)
    if not append:
        basins.append([(i,j)])
    

@time_function
def puzzle2(data):
    M = len(data)
    N = len(data[0])
    l = [list(zip([x] * N, range(N))) for x in range(M)]
    l = reduce(lambda x,y : x+y, l)
    data = reduce(lambda x,y : x+y, data)
    # Depthmap:
    depth = dict(zip(l, data))
    check_coordinates = [k for k in depth if depth[k] != 9]
    basins = []
    # for i in range(M):
    #     for j in range(N):
    #         if (i,j) in check_coordinates:
    #             check_in_existing_basin(i,j, basins)
    for i,j in check_coordinates:
        check_in_existing_basin(i, j, basins)
    return reduce(lambda x, y: x * y, sorted([len(b) for b in basins], reverse=True)[:3] )

if __name__ == '__main__':
    with open(DIR / 'input.txt') as f:
        data = [line.rstrip() for line in f.readlines()]
        data = list(map(lambda x: list(map(int, x)),  data))

    # Puzzle 1
    print(f"Puzzle 1: {puzzle1(data)}")
    # Puzzle 2
    print(f"Puzzle 2: {puzzle2(data)}")

'''
Function puzzle1(<class 'list'>,): time elapsed: 190.456 [ms]
Puzzle 1: 607
Function puzzle2(<class 'list'>,): time elapsed: 2307.369 [ms]
Puzzle 2: 900864
Function puzzle2(<class 'list'>,): time elapsed: 1410.200 [ms]
Puzzle 2: 900864
'''