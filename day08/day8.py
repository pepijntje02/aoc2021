import sys, pathlib
from typing import Collection
DIR = pathlib.Path(__file__).parent
parentdir = DIR.resolve().parent # Get root direcotry AOC
sys.path.append(str(parentdir))
from myDecorator import time_function

from collections import defaultdict, namedtuple

def process_input(data):
    Input = namedtuple("Input", ["unique_signal", "output_value"])
    return [Input(*map(lambda x: x.split(), i)) for i in [d.split('|') for d in data]]


@time_function
def puzzle1(data):
    # unique lengths: 1:2, 4:4, 7:3, 8:7
    # Output values are at index 1 of data
    Output = list(zip(*data))[1]
    f = lambda x: len(x) in [2, 4, 3, 7]
    return sum( [sum(map(f, u)) for u in Output] )


def process_line(line):
    # Get positions form unique
    # line = 'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc'
    # line = 'be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe'
    # line = process_input([line])[0]
    # print(line)
    unique, output = line
    # Position in the clock
    # signal_pattern = {k:'abcdefg' for k in range(9)}
    signal_pattern = {k:'' for k in range(10)}
    # fill with unique:
    u = {2:1, 4:4, 3:7, 7:8}
    for group in unique:
        if len(group) in u:
            signal_pattern[u[len(group)]] = group
            unique.remove(group)
            
    position = {
        0 : [0, 1, 2, 4, 5, 6],
        1 : [2, 5],
        2 : [0, 2, 3, 4, 6],
        3 : [0, 2, 3, 5, 6],
        4 : [1, 2, 3, 5],
        5 : [0, 1, 3, 5, 6],
        6 : [0, 1, 3, 4, 5, 6],
        7 : [0, 2, 5],
        8 : [0, 1, 2, 3, 4, 5, 6],
        9 : [0, 1, 2, 3, 5, 6]
    }

    # create clock:
    clock = ['abcdefg']*7
    # check for unique values:
    for k, v in signal_pattern.items():
        if len(v) > 0:
            for pos in position[k]:
                if len(clock[pos]) == 7:
                    clock[pos] = v
    
    # initialization of the clock is done
    # check if value can be centered at a selection of places:
    def check_clock(clock, changed=False):
        clock.copy()
        for c in clock:
            if clock.count(c) == len(c):
                for i, cc in enumerate(clock):
                    for char in c:
                        if char in cc and len(cc) != len(c):
                            changed = True
                            clock[i] = clock[i].replace(char, '')
        if changed:
            return check_clock(clock)
        return clock

    clock = check_clock(clock)

    def unique_gen(arr):
        i = -1
        while len(arr) > 0:
            i+=1
            if i == len(arr):
                i = 0
            yield arr[i]

    gen = unique_gen(unique)
    for u in gen:
        # which position is sure:
        sure = []
        possible = []
        # unkown_values = []
        for i, c in enumerate(clock):
            if len(set(c).intersection(set(u))) == len(c):
                sure += [i for i, cl in enumerate(clock) if c in cl]
            elif len(set(c).intersection(set(u))) > 0:
                possible += [(i, ''.join(set(c).intersection(set(u)))) for i, cl in enumerate(clock) if cl in c]
        # which are sure:
        sure = set(sure)
        possible = dict(set(possible))

        digits = [k for k, v in position.items() if len(sure.intersection(v)) == len(sure) \
            and len(u) == len(v)]

        if len(digits) == 1:
            signal_pattern[digits[0]] = u
            # unkown:
            unkown = set(possible.keys()).intersection(set(position[digits[0]]))
            for u in unkown:
                clock[u] = ''.join(possible[u])
            clock = check_clock(clock)
        if sum( [len(x) == 1 for x in clock]) == len(clock):
            break
        # if sum([sorted(o) in list(map(sorted, signal_pattern.values())) for o in output]):
        #     break


    # clock is unique:
    for k, v in signal_pattern.items():
        if len(v) == 0:
            signal_pattern[k] = ''.join([clock[i] for i in position[k]])
    # sort:
    lookup = {}
    for k, v in signal_pattern.items():
        lookup[''.join(sorted(v))] = str(k)
    # get digits:
    return int(''.join([lookup[''.join(sorted(key))] for key in output]))

@time_function
def puzzle2(data):
    res = []
    for line in data:
        res.append(process_line(line))
        # print(res[-1])
    return sum(res)

if __name__ == '__main__':
    with open(DIR / 'input.txt') as f:
        data = [line.rstrip() for line in f.readlines()]
        try:
            data = list(map(float, data))
        except:
            pass
    data = process_input(data)
    # Puzzle 1
    print(f"Puzzle 1: {puzzle1(data)}")
    # Puzzle 2
    print(f"Puzzle 2: {puzzle2(data)}")

'''
Function puzzle1(<class 'list'>,): time elapsed: 0.240 [ms]
Puzzle 1: 261
Function puzzle2(<class 'list'>,): time elapsed: 68.536 [ms]
Puzzle 2: 987553
'''
