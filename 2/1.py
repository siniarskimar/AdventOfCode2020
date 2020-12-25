import sys
import re
inp = open("input", "r")
inp_lines = inp.readlines()
data = []
valid_pass = 0

# Parse input
for i in range(len(inp_lines)):
    match = re.match("^([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)", inp_lines[i])
    data.append([
        int(match.group(1)),int(match.group(2)),match.group(3), match.group(4)
    ])

for i in range(len(data)):
    count = 0
    for c in range(len(data[i][3])):
        if data[i][3][c] == data[i][2]:
            count = count + 1
    if count >= data[i][0] and count <= data[i][1]:
        valid_pass = valid_pass + 1

print(valid_pass)