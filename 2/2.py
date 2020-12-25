import sys
import re
inp = open("input", "r")
inp_lines = inp.readlines()
cases = []
valid_pass = 0

class Case():
    def __init__(self, pos1,pos2, letter, password):
        self.pos1 = pos1
        self.pos2 = pos2
        self.letter = letter
        self.password = password
        

# Parse input
for i in range(len(inp_lines)):
    match = re.match("^([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)", inp_lines[i])
    cases.append(
        Case(int(match.group(1)),int(match.group(2)),match.group(3), match.group(4))
    )

for i in range(len(cases)):
    count = 0
    case = cases[i]
    #print("{0}-{1} {2}: {3}".format(case.pos1,case.pos2,case.letter,case.password))

    if case.password[case.pos1-1] == case.letter:
        count = count + 1
    if case.password[case.pos2-1] == case.letter:
        count = count + 1

    if count == 1:
        valid_pass = valid_pass + 1

print(valid_pass)