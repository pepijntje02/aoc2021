from os import name
import sys, pathlib
DIR = pathlib.Path(__file__).parent
parentdir = DIR.resolve().parent # Get root direcotry AOC
sys.path.append(str(parentdir))
from myDecorator import time_function

from collections import namedtuple

def hex2bin(string, nbits=4):
    '''
    Turn hexadecimal character to nbits
    '''
    return ''.join( map(lambda x: bin(int(x, 16))[2:].zfill(nbits), string) ) 

# class Package:
#     def __init__(self, BITS):
#         self.version = int(BITS[:3],2)
#         self.type_id = int(BITS[3:6], 2)
#         BITS = BITS[6:]
#         if self.type_id != 4:
#             self.length_ID = BITS[0]
#             BITS = BITS[1:]
#             if int(self.length_ID) == 0:
#                 self.length = int(BITS[:15], 2)
#             else:
#                 self.n_subpackets = int(BITS[:11], 2)

Package = namedtuple("Package", ['version', 'type', 'value'])

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
            BITS = BITS[13:]
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
    v = 0
    

@time_function
def puzzle1(BITS:str)->int:
    p, b = add_package(BITS)

    pass

@time_function
def puzzle2(data):
    pass

if __name__ == '__main__':
    with open(DIR / 'input.txt') as f:
        data = f.readlines()
    sample = 'D2FE28'
    sample = '38006F45291200'
    sample = '620080001611562C8802118E34'
    BITS = hex2bin(sample)
    BITS = hex2bin(data)
    # Puzzle 1
    print(f"Puzzle 1: {puzzle1(data)}")
    # Puzzle 2
    print(f"Puzzle 2: {puzzle2(data)}")
