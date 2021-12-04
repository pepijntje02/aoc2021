import sys, pathlib
parentdir = pathlib.Path(__file__).resolve().parents[1] # Get root direcotry AOC
sys.path.append(str(parentdir))
from myDecorator import time_function

def read_bingo(data):
    board = []
    boards = []
    for i, line in enumerate(data):
        if i == 0:
            numbers = list(map(int, line.split(',')))
        else:
            if len(line) > 1:
                board.append(list(map(int, filter(None, line.split(' ')))))
            elif len(board) > 1:
                boards.append(Bingo(board))
                board = []
    if len(board) > 1:
        boards.append(Bingo(board))
    return numbers, boards

class Bingo:
    def __init__(self, board):
        self.board = board
        self.marked = [[0 for _ in board[0]] for _ in board]

    def play_number(self, number):
        for i, row in enumerate(self.board):
            try:
                idx = row.index(number)
                self.marked[i][idx] = 1
            except:
                pass
        return self.check_score()
    
    def check_score(self):
        for row in self.marked + list(zip(*self.marked)):
            if sum(row) == len(row):
                return True

    def calc_unmarked_numbers(self):
        s = 0
        for row_board, row_marked in zip(self.board, self.marked):
            s += sum([b for b, m in zip(row_board, row_marked) if m != 1])
        return s


@time_function
def puzzle1(data):
    numbers, boards = read_bingo(data)
    for n in numbers:
        for bingo in boards:
            if bingo.play_number(n):
                return bingo.calc_unmarked_numbers() * n

@time_function
def puzzle2(data):
    numbers, boards = read_bingo(data)
    for n in numbers:
        for i  in range(len(boards)-1, -1, -1):
            bingo = boards[i]
            if bingo.play_number(n) and len(boards) > 1:
                boards.pop(i)
            elif bingo.play_number(n):
                return bingo.calc_unmarked_numbers() * n

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
Function puzzle1(<class 'list'>,): time elapsed: 13.769 [ms]
Puzzle 1: 44088
Function puzzle2(<class 'list'>,): time elapsed: 55.310 [ms]
Puzzle 2: 23670 
'''
