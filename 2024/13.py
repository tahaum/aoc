import numpy as np
import re

from utils.io import read_input

data_path = "data/input_13.txt"
data = read_input(data_path)


def parse_input(data: str, add: float) -> list:
    machines = list()
    for block in data.split("\n\n"):
        ints = [float(i) for i in re.findall(r"\d+", block)]
        a, b, prize = ints[:2], ints[2:4], ints[4:]
        machines.append((a, b, [p + add for p in prize]))
    return machines


def solve_linear_equation(a, b, x) -> int:
    M = np.stack([a, b])
    sol = np.rint(np.linalg.solve(M.transpose(), x))
    return sol @ (3, 1) if np.all(sol @ M == x) else 0


def solve(data: str, add: float = 0.0):
    machines = parse_input(data, add)
    return int(sum([solve_linear_equation(*m) for m in machines]))


print("Part 1:", solve(data))
print("Part 2:", solve(data, 10000000000000))
