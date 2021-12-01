with open('./input.txt') as f:
    data = [float(line) for line in f.readlines()]

def increase(data):
    f = lambda x, y: y > x
    return sum( list(map(f, data[:-1], data[1:])) )

puzzle1 = increase(data)
print(puzzle1)

def sliding_window(array):
    return [sum(array[i:i+3]) for i in range(len(array)-2)]

three_sum = sliding_window(data)

puzzle2 = increase(three_sum) 
print(puzzle2)
