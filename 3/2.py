lines = open("input.txt","r").readlines()

# Get rid of newlines
for i in range(len(lines)):
    lines[i] = lines[i][0:-1]

def descend(desc_x, desc_y):
    width = len(lines[0])
    height = len(lines)
    x = 0
    y = 0
    count = 0

    while y < height:
        if x >= width:
            x = x % width
        if lines[y][x] == '#':
            count = count + 1
        x = (x + desc_x)
        y = y + desc_y
    return count

mul = descend(1,1) * descend(3,1) * descend(5,1) * descend(7,1) * descend(1,2)
print(mul)