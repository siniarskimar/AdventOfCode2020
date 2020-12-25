import re
inp = open("input.txt", "r").readlines()
valid = 0
n = len(inp)
# Array of found keys
passport = []

for i in range(n):
    #print("line: ", inp[i])
    if inp[i][0] == '\n':
        print(passport, end=' ')
        req = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        for j in range(len(passport)):
            if passport[j] in req:
                index = req.index(passport[j])
                del req[index:index+1]
        if len(req) == 0:
            valid = valid + 1
        print(req)
        del passport[:]
    else:
        match = re.findall("([a-z]+):", inp[i])
        passport.extend(match)

print(valid)