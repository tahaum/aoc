from utils.io import read_input
from collections import Counter

data_path = "data/input_01.txt"
data = read_input(data_path).splitlines()
L, R = [], []
for row in data:
    l, r = (int(nr) for nr in row.split())
    L.append(l)
    R.append(r)

def solve_p1(L, R):
    L = sorted(L)
    R = sorted(R)
    
    diff = 0
    for l, r in zip(L, R):
        diff += abs(l - r)
    return diff

def solve_p2(L, R):
    tot = 0
    counter = Counter(R)
    for l in L:
        if l in R:
            tot += l * counter.get(l)
    return tot

print("Part 1:", solve_p1(L, R))
print("Part 2:", solve_p2(L, R))
