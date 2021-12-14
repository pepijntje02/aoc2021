import sys, pathlib
DIR = pathlib.Path(__file__).parent
parentdir = DIR.resolve().parent # Get root direcotry AOC
sys.path.append(str(parentdir))
from myDecorator import time_function

from collections import defaultdict, Counter
from itertools import chain

def pair_insertion(string, template):
    s = list(map(list, zip(string[:-1], string[1:])))
    # s = list(map(lambda x: ''.join(x), s))
    for char in s:
        c = template.get(''.join(char), None)
        if c:
            char.insert(1, c)
    return ''.join(list(map(lambda x: ''.join(x[:-1]), s))) + s[-1][-1]
    # return ''.join(s) + s[-1]

@time_function
def puzzle1(string, template, n=10):
    for _ in range(n):
        string = pair_insertion(string, template)
    count = [string.count(char) for char in set(string)]
    return max(count) - min(count)

def pair_insertion_v2(d, template, counter):
    d_new = defaultdict(int)
    for key, count in d.items():
        c = template.get(key, None)
        if c:
            # add counter:
            counter[c] += count
            # add new pairs to dict:
            pair1 = key[0] + c
            pair2 = c + key[1]
            d_new[pair1] += count
            d_new[pair2] += count
    return d_new, counter

@time_function
def puzzle2(string, template, n):
    counter = Counter(string)
    pairs = zip(string[:-1], string[1:])
    d = defaultdict(int)
    for ele in pairs:
        d[''.join(ele)] += 1
    # template = {(k[0], k[1]):v for k,v in template.items()}
    for _ in range(n):
        d, counter = pair_insertion_v2(d, template, counter)
    values = counter.values()
    return max(values) - min(values)

if __name__ == '__main__':
    with open(DIR / 'input.txt') as f:
        data = [line.rstrip() for line in f.readlines()]
    start = data[0]
    l = list(zip(*(map(lambda x: x.split(' -> '), data[2:]))))
    template = dict(zip(*l))
    # Puzzle 1
    print(f"Puzzle 1: {puzzle1(start, template)}")
    print(f"Puzzle 1: {puzzle2(start, template, n=10)}")
    # Puzzle 2
    print(f"Puzzle 2: {puzzle2(start, template, n=40)}")

'''
Function puzzle1(<class 'str'>, <class 'dict'>): time elapsed: 12.199 [ms]
Puzzle 1: 2435
Function puzzle2(<class 'str'>, <class 'dict'>, "n=<class 'int'>"): time elapsed: 0.605 [ms]
Puzzle 1: 2435
Function puzzle2(<class 'str'>, <class 'dict'>, "n=<class 'int'>"): time elapsed: 2.424 [ms]
Puzzle 2: 2587447599164
'''
