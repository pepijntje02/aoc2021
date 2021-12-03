import sys, pathlib
parentdir = pathlib.Path(__file__).parents[1] # Get root direcotry AOC
sys.path.append(str(parentdir))
from myDecorator import time_function

class Position_puzzle1:
    def __init__(self) -> None:
        self.horizontal = 0
        self.depth = 0
    
    def forward(self, x):
        self.horizontal += x
    
    def down(self, x):
        self.depth += x
    
    def up(self, x):
        self.depth -= x
    
    def process_line(self, line):
        x = int(line.split(' ')[1])
        if 'forward' in line:
            self.forward(x)
        elif 'up' in line:
            self.up(x)
        elif 'down' in line:
            self.down(x)

class Position_puzzle2:
    def __init__(self) -> None:
        self.horizontal = 0
        self.depth = 0
        self.aim = 0
    
    def forward(self, x):
        self.horizontal += x
        self.depth += x * self.aim
    
    def down(self, x):
        self.aim += x
    
    def up(self, x):
        self.aim -= x
    
    def process_line(self, line):
        x = int(line.split(' ')[1])
        if 'forward' in line:
            self.forward(x)
        elif 'up' in line:
            self.up(x)
        elif 'down' in line:
            self.down(x)

@time_function
def puzzle1(data):
    pos = Position_puzzle1()
    for line in data:
        pos.process_line(line)
    return pos.horizontal * pos.depth

@time_function
def puzzle2(data):
    pos = Position_puzzle2()
    for line in data:
        pos.process_line(line)
    return pos.horizontal * pos.depth

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

'''
Function puzzle1(<class 'list'>,): time elapsed: 0.476 [ms]
Puzzle 1: 1692075
Function puzzle2(<class 'list'>,): time elapsed: 0.806 [ms]
Puzzle 2: 1749524700
'''