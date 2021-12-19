from os import name
import sys, pathlib
DIR = pathlib.Path(__file__).parent
parentdir = DIR.resolve().parent # Get root direcotry AOC
sys.path.append(str(parentdir))
from myDecorator import time_function

# from collections import namedtuple
# Package = namedtuple("Package", ['version', 'type', 'value'])
from functools import reduce

class Package:
    def __init__(self, version, type_id, value):
        self.version = version
        self.type = type_id
        self.value = value
    def __str__(self):
        return f"version: {self.version}, type:{self.type}, value:{self.value}"
    def __repr__(self):
        return self.__str__()
    def calc_value(self):
        if type(self.value) != list:
            return self.value
        # Check that each subpackage (in list value) is an integer:
        for subpackage in self.value:
            if type(subpackage.value) == list:
                subpackage.value = subpackage.calc_value()
        value = [subpackage.value for subpackage in self.value]
        # for each type:
        if self.type == 0:
            self.value = sum(value)
        elif self.type == 1:
            self.value = reduce(lambda x,y: x*y, value)
        elif self.type == 2:
            self.value = min(value)
        elif self.type == 3:
            self.value = max(value)
        elif self.type == 5:
            self.value = int(value[0] > value[1])
        elif self.type == 6:
            self.value = int(value[0] < value[1])
        elif self.type == 7:
            self.value = int(value[0] == value[1])
        return self.value


def hex2bin(string, nbits=4):
    '''
    Turn hexadecimal character to nbits
    '''
    return ''.join( map(lambda x: bin(int(x, 16))[2:].zfill(nbits), string) ) 

def add_package(BITS):
    version = int(BITS[:3], 2)
    type_id = int(BITS[3:6], 2)
    BITS = BITS[6:]
    # Create new package:
    if type_id != 4: # operator
        length_type_id = int(BITS[0])
        if length_type_id == 0:
            n = int(BITS[1:16], 2)
            BITS = BITS[16:]
            v = []
            BITSCOPY = BITS[:n]
            while len(BITSCOPY) >0:
                p, BITSCOPY = add_package(BITSCOPY)
                v.append(p)
            return Package(version, type_id, v), BITS[n:]
        if length_type_id == 1:
            n = int(BITS[1:12], 2)
            BITS = BITS[12:]
            v = []
            for _ in range(n):
                p, BITS = add_package(BITS)
                v.append(p)
            return Package(version, type_id, v), BITS
    else:
        # padd zeros:
        bits_old = BITS
        while (len(BITS) + 6) % 4 != 0: # add 6 since BITS is resized at the start.
            BITS += '0'
        number = ''
        while True:
            bit = int(BITS[0])
            number += BITS[1:5]
            BITS = BITS[5:]
            bits_old = bits_old[5:]
            if bit == 0:
                if len(BITS) == 0:
                    BITS = None
                return Package(version, type_id, int(number, 2)), bits_old

def get_versions(packages):
    v = packages.version
    if type(packages.value) == list:
        for p in packages.value:
            v+=get_versions(p)
    return v

@time_function
def puzzle1(BITS:str)->int:
    p, _ = add_package(BITS)
    # Get all versions:
    return get_versions(p)

@time_function
def puzzle2(BITS:str)->int:
    p, _ = add_package(BITS)
    return p.calc_value()

if __name__ == '__main__':
    with open(DIR / 'input.txt') as f:
        data = f.read().rstrip()
    sample = '9C0141080250320F1802104A08'
    BITS = hex2bin(sample)
    BITS = hex2bin(data)
    # Puzzle 1
    print(f"Puzzle 1: {puzzle1(BITS)}")
    # Puzzle 2
    print(f"Puzzle 2: {puzzle2(BITS)}")
