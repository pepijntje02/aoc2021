import sys, pathlib
parentdir = pathlib.Path(__file__).resolve().parents[1] # Get root direcotry AOC
sys.path.append(str(parentdir))
from myDecorator import time_function

import re
from collections import defaultdict, namedtuple

def add_hor_vert_line(d:defaultdict, point1:namedtuple, point2:namedtuple):
    dx = point2.x - point1.x
    dy = point2.y - point1.y
    if dx != 0 and dy==0:
        if dx < 0:
            point1, point2 = point2, point1
            dx *= -1
        for x in range(point1.x, point2.x +1):
            d[(x, point1.y)] += 1
    elif dy != 0 and dx==0:
        if dy < 0:
            point1, point2 = point2, point1
            dy *= -1
        for y in range(point1.y, point2.y +1):
            d[(point1.x, y)] += 1

def get_lines(data):
    reg = re.compile(r'(\d+),(\d+).*\s(\d+),(\d+)')
    Point = namedtuple("Point", "x y")
    f = lambda x: [Point(x[0], x[1]), Point(x[2], x[3])]
    lines =  [list(map(int, reg.search(line).groups())) for line in data]
    return list(map(f, lines))

def get_hor_vert_lines(lines):
    danger = defaultdict(lambda : 0)
    for point1, point2 in lines:
        add_hor_vert_line(danger, point1, point2)
    return danger

@time_function
def puzzle1(data):
    lines = get_lines(data)
    danger = get_hor_vert_lines(lines)
    ans = namedtuple("ans", ['puzzle1', 'lines', 'dict'])
    return ans(sum([v >= 2 for v in danger.values()]), lines, danger)

def add_diagonal_line(d:defaultdict, point1:namedtuple, point2:namedtuple):
    dx = point2.x - point1.x
    dy = point2.y - point1.y
    # 45 degree:
    if abs(dx) != abs(dy):
        return
    if dx != 0 and dy != 0:
        direction_x = 1 if dx >= 0 else -1
        direction_y = 1 if dy >= 0 else -1
        for x, y in zip(range(point1.x, point2.x + direction_x, direction_x),
                range(point1.y, point2.y + direction_y, direction_y)):
            d[(x,y)] += 1

@time_function
def puzzle2(lines, danger):
    for point1, point2 in lines:
        add_diagonal_line(danger, point1, point2)
    return sum([v >= 2 for v in danger.values()])

if __name__ == '__main__':
    with open('./input.txt') as f:
        data = [line.rstrip() for line in f.readlines()]
        try:
            data = list(map(float, data))
        except:
            pass
    # Puzzle 1
    p1 = puzzle1(data)
    print(f"Puzzle 1: {p1.puzzle1}")
    # Puzzle 2
    p2 = puzzle2(p1.lines, p1.dict)
    print(f"Puzzle 2: {p2}")
