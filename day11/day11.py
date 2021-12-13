import sys, pathlib
DIR = pathlib.Path(__file__).parent
parentdir = DIR.resolve().parent # Get root direcotry AOC
sys.path.append(str(parentdir))
from myDecorator import time_function

from collections import defaultdict

def calc_coords(i,j, n=3, offset=1):
    return [(a,b) for b in range(j-offset, j + n - offset) for a in range(i-offset, i - offset + n)]

def flash(d, old_coords = []):
    # print("Call FLASH:")
    if len(old_coords) == 0:
        for key in d:
            d[key] += 1
    coords = []
    for k, v in d.items():
        if v > 9:
            coords.append(k)
    coords = set(coords)
    old_coords = set(old_coords)
    coords = coords & old_coords ^ coords
    # old_coords = list(old_coords)
    if len(coords) > 0:
        for coord in coords:
            c = calc_coords(*coord)
            # Only coords in coordlist
            old_coords |= set([coord])
            c = set(c) & set(d.keys()) - old_coords
            d[coord] = 0
            for coord in c:
                d[coord] += 1
        return flash(d, old_coords)
    return d, len(old_coords)

def to_matrix(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

def matrix_to_string(m):
    return [','.join([f"{ele: >3}" for ele in subset]) for subset in m]

@time_function
def puzzle1(data, steps=100):
    d = defaultdict(int, zip(calc_coords(0, 0, n=10, offset=0), 
        [item for sublist in data for item in sublist]))
    total = 0
    for _ in range(steps):
        d, t = flash(d)
        total += t
    return d, total

@time_function
def puzzle2(data):
    d = defaultdict(int, zip(calc_coords(0, 0, n=10, offset=0), 
        [item for sublist in data for item in sublist]))
    step = 0
    while True:
        step += 1
        d, t = flash(d)
        if sum(d.values()) == 0:
            break
    return step
    pass

if __name__ == '__main__':
    with open(DIR / 'input.txt') as f:
        data = [list(map(int, line.rstrip())) for line in f.readlines()]
    with open(DIR / 'sample.txt') as f:
        sample = [list(map(int, line.rstrip())) for line in f.readlines()]
    # Puzzle 1
    d, total = puzzle1(sample, steps=100)
    print(f"Puzzle 1: {total}")
    # m = to_matrix(list(d.values()), 10)
    # print( *matrix_to_string(m), sep='\n' )
    # Puzzle 2
    print(f"Puzzle 2: {puzzle2(data)}")

'''
Function puzzle1(<class 'list'>, "steps=<class 'int'>"): time elapsed: 21.429 [ms]
Puzzle 1: 1656
Function puzzle2(<class 'list'>,): time elapsed: 74.280 [ms]
Puzzle 2: 360
'''