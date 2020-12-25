import sys
import os
import fileinput

if sys.stdin.isatty():
    os.exit()

X = [int(line) for line in fileinput.input()]
n = len(X)

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1, n):
            if i != j and X[i] + X[j] + X[k] == 2020:
                print(X[i]*X[j]*X[k])