from itertools import product

from utils.io import read_input

data_path = "data/input_07.txt"
data = read_input(data_path).splitlines()

OPS = ["+", "*", "||"]


def parse_input(data: list) -> list:
    equations = []
    for row in data:
        test_value, numbers = row.split(":")
        equations.append((int(test_value), numbers.split()))
    return equations


def correct_brute(eq: tuple, concat: bool = False) -> bool:
    val, nums = eq
    n_ops = len(nums) - 1
    ops = OPS[:2] if not concat else OPS
    permus = product(ops, repeat=n_ops)
    for permu in permus:
        sum_ = 0
        for i in range(n_ops):
            a = nums[i] if i == 0 else sum_
            b = nums[i + 1]
            if permu[i] != "||":
                sum_ = eval(f"{a} {permu[i]} {b}")
            else:
                sum_ = int(str(a) + b)
            if sum_ > val:
                break
        if sum_ == val:
            return True
    return False


def solve(data: list, concat: bool = False) -> int:
    eqs = parse_input(data)
    return sum([eq[0] if correct_brute(eq, concat) else 0 for eq in eqs])


print("Part 1:", solve(data))
print("Part 2:", solve(data, True))
