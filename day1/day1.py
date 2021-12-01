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

# And now with thinking, i.e. use math instead of brute force
# If the list is: 0, 1, 2, 3, 4 then the moving difference is:
# (1 + 2 + 3) - (0 + 1 + 2) = 3-0 i.e. index 0 and index 2.
# Rewrite increase function:

def increasev2(data, step):
    f = lambda x, y: y > x
    return sum( list(map(f, data[:-step], data[step:])) )

print(increasev2(data, step=3))