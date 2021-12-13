import sys, pathlib
DIR = pathlib.Path(__file__).parent
parentdir = DIR.resolve().parent # Get root direcotry AOC
sys.path.append(str(parentdir))
from myDecorator import time_function

from collections import defaultdict

@time_function
def puzzle1(data):
    # Get all paths (forward and backward)
    paths = defaultdict(list)
    for line in data:
        node1, node2 = line.split('-')
        paths[node1].append(node2)
        if node1 != 'start':
            paths[node2].append(node1)
    paths['end'] = []
    startnode = 'start'
    return len(get_paths(startnode, paths))

def get_paths(node, paths, visited=[]):
    n_paths = []
    visited.append(node)
    for children in paths[node]: 
        if not (children.islower() and children in visited):
            n_paths.extend(get_paths(children, paths, visited.copy()))
    if visited[-1] == 'end':
        n_paths.append(visited)
    return n_paths

@time_function
def puzzle2(data):
    paths = defaultdict(list)
    for line in data:
        node1, node2 = line.split('-')
        paths[node1].append(node2)
        if node1 != 'start':
            paths[node2].append(node1)
    paths['end'] = []
    startnode = 'start'
    return len(get_paths_twice(startnode, paths))

def get_paths_twice(node, paths, visited=[]):
    n_paths = []
    visited.append(node)
    for children in paths[node]: 
        again = True
        if children.islower():
            visited_lower = [v for v in visited if v.islower()]
            if (len(set(visited_lower)) == len(visited_lower)-1 and children in visited) \
                or children == 'start':
                again = False
        if again:
            n_paths.extend(get_paths_twice(children, paths, visited.copy()))
    if visited[-1] == 'end':
        n_paths.append(visited)
    return n_paths

if __name__ == '__main__':
    with open(DIR / 'input.txt') as f:
        data = [line.rstrip() for line in f.readlines()]
    # with open(DIR / 'sample.txt') as f:
    #     data = [line.rstrip() for line in f.readlines()]
    # Puzzle 1
    print(f"Puzzle 1: {puzzle1(data)}")
    # Puzzle 2
    print(f"Puzzle 2: {puzzle2(data)}")
