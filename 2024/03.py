import re

from utils.io import read_input

data_path = "data/input_03.txt"
data = read_input(data_path)


def solve_p1(data: str) -> int:
    muls = re.findall("mul\((\d+),(\d+)\)", data)
    return sum([int(mul[0]) * int(mul[1]) for mul in muls])


def solve_p2(data: str) -> int:
    pat = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"
    sum_ = 0
    do = True
    for m in re.finditer(pat, data):
        if m.group(0) == "do()":
            do = True
        elif m.group(0) == "don't()":
            do = False
        else:
            if do:
                sum_ += int(m.group(1)) * int(m.group(2))
    return sum_


print("Part 1:", solve_p1(data))
print("Part 2:", solve_p2(data))
