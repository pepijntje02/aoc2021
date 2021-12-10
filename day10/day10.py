import sys, pathlib
DIR = pathlib.Path(__file__).parent
parentdir = DIR.resolve().parent # Get root direcotry AOC
sys.path.append(str(parentdir))
from myDecorator import time_function

@time_function
def puzzle1(data):
    #apply to each line:
    pairs = '()[]{}<>'
    opening = pairs[::2]
    closing = pairs[1::2]
    pairs = dict(zip(closing, opening))
    missed = []
    correct_lines = []
    for line in data:
        incomplete = True
        open_char = []
        for char in line:
            if char in closing:
                try:
                    if open_char[-1] == pairs[char]:
                        open_char.pop(-1)
                    else:
                        missed.append(char)
                        incomplete = False
                        break
                except:
                    missed.append(char)
                    break
            else:
                open_char.append(char)
        if incomplete:
            correct_lines.append(line)
    # values:
    v = dict(zip(closing, [3, 57, 1197, 25137]))
    return sum([missed.count(i)*v[i] for i in set(missed)]), correct_lines

@time_function
def puzzle2(incomplete):
    pairs = '()[]{}<>'
    opening = pairs[::2]
    closing = pairs[1::2]
    pairs = dict(zip(closing, opening))
    closing_pairs = dict(zip(opening, closing))
    v = dict(zip(closing, [1, 2, 3, 4]))
    
    complete = []
    for line in incomplete:
        open_char = []
        for char in line:
            if char in closing:
                try:
                    if open_char[-1] == pairs[char]:
                        open_char.pop(-1)
                except:
                    pass
            else:
                open_char.append(char)
        complete.append( [closing_pairs[v] for v in open_char[::-1]] )
    
    score = []
    for missing in complete:
        s = 0
        for c in missing:
            s = s*5 + v[c]
        score.append(s)
    return sorted(score)[len(score) // 2]


if __name__ == '__main__':
    with open(DIR / 'input.txt') as f:
        data = [line.rstrip() for line in f.readlines()]
    # Puzzle 1
    p1, incomplete = puzzle1(data)
    print(f"Puzzle 1: {p1}")
    # Puzzle 2
    print(f"Puzzle 2: {puzzle2(incomplete)}")
