from collections import defaultdict
from utils.io import read_input

data_path = "data/input_19.txt"
data = read_input(data_path)


def parse_input(data):
    towels, designs = data.split("\n\n")
    return towels.split(", "), designs.splitlines()


TOWELS, DESIGNS = parse_input(data)
DP = {}


def possible_ways(design: str) -> int:
    if design in DP:
        return DP[design]
    ans = 0
    if len(design) == 0:
        return 1
    for towel in TOWELS:
        if design.startswith(towel):
            ans += possible_ways(design[len(towel) :])
    DP[design] = ans
    return ans


def solve() -> int:
    p1, p2 = 0, 0
    for design in DESIGNS:
        ways = possible_ways(design)
        if ways > 0:
            p1 += 1
        p2 += ways
    return p1, p2


p1, p2 = solve()
print("Part 1:", p1)
print("Part 2:", p2)
