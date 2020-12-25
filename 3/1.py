lines = open("input.txt","r").readlines()

# Get rid of newlines
for i in range(len(lines)):
    lines[i] = lines[i][0:-1]

width = len(lines[0])
height = len(lines)
x = 0
y = 0
count = 0

while y != height:
    if lines[y][x] == '#':
        count = count + 1
    x = (x + 3) % width
    y = y + 1

print(count)