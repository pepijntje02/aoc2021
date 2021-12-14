import sys, pathlib
DIR = pathlib.Path(__file__).parent
parentdir = DIR.resolve().parent # Get root direcotry AOC
sys.path.append(str(parentdir))
from myDecorator import time_function

from collections import namedtuple, defaultdict
import re

Coord = namedtuple("Coord", ['x', 'y'])

def fold(command, pos):
    command_line = {'x':0, 'y':1}
    keys = list(pos.keys())
    check = list(zip(*keys))[command_line[command.axis]]
    # coords = list(zip(*keys))
    bool_arr = [value > command.line for value in check]
    while any(bool_arr):
        idx = bool_arr.index(True)
        # new coordinate:
        x, y = keys[idx]
        del pos[keys[idx]]
        if command.axis == 'x':
            x = 2*command.line - x
        else:
            y = 2*command.line - y
        pos[Coord(x,y)] += 1
        bool_arr.pop(idx)
        keys.pop(idx)
    return pos

@time_function
def puzzle1(coords, commands):
    pos = defaultdict(lambda: 1)
    [pos[c] for c in coords]
    pos = fold(commands[0], pos)
    return len(pos)

@time_function
def puzzle2(coords, commands):
    pos = defaultdict(lambda: 1)
    [pos[c] for c in coords]
    for command in commands:
        pos = fold(command, pos)
    # plot pos:
    # create string with dots:
    width = max(list(zip(*pos.keys()))[0]) + 1
    height = max(list(zip(*pos.keys()))[1]) + 1
    # create string:
    grid = [[' '] * width for _ in range(height)]
    for key in pos.keys():
        grid[key.y][key.x] = '#'
    print(*[''.join(row) for row in grid], sep='\n')
    return None

if __name__ == '__main__':
    with open(DIR / 'input.txt') as f:
        data = [line.rstrip() for line in f.readlines()]
        coords = [d for d in data if len(d.split(',')) > 1]
        commands = [c for c in data[len(coords):] if len(c) >0]
    Command = namedtuple("Command", ['axis', 'line'])
    coords = [Coord(*map(int, c.split(','))) for c in coords]
    commands = list(map(lambda x: re.compile(r'([x|y])=(\d+)').search(x).groups(), commands))
    commands = [Command(x[0], int(x[1])) for x in commands]
    # Puzzle 1
    print(f"Puzzle 1: {puzzle1(coords, commands)}")
    # Puzzle 2
    print(f"Puzzle 2: {puzzle2(coords, commands)}")
'''
Function puzzle1(<class 'list'>, <class 'list'>): time elapsed: 2.392 [ms]
Puzzle 1: 788
#  #   ## ###  #  # #### #  # ###   ##
# #     # #  # # #  #    #  # #  # #  #
##      # ###  ##   ###  #  # ###  #
# #     # #  # # #  #    #  # #  # # ##
# #  #  # #  # # #  #    #  # #  # #  #
#  #  ##  ###  #  # ####  ##  ###   ###
Function puzzle2(<class 'list'>, <class 'list'>): time elapsed: 10.071 [ms]
Puzzle 2: None
'''