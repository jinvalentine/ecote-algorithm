a = input()
row = int(a[1])
column = int(ord(a[0]) - ord("a")) + 1


result = 0

steps = [(-2, -1), (-2, 1), (2, 1), (2, -1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)