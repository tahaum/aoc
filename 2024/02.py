from utils.io import read_input

data_path = "data/input_02.txt"
data = read_input(data_path).splitlines()


def is_safe(r: list) -> bool:
    safe = True
    ascending = r[0] < r[-1]
    for i in range(1, len(r)):
        if (
            r[i] == r[i - 1]
            or (abs(r[i] - r[i - 1]) > 3)
            or (r[i] > r[i - 1] and not ascending)
            or (r[i] < r[i - 1] and ascending)
        ):
            safe = False
    return safe


def is_safe_dampened(r: list) -> bool:
    for i in range(0, len(r)):
        r_ = r.copy()
        r_.pop(i)
        if is_safe(r_):
            return True
    return False


def solve(data: list, dampen: bool = False) -> int:
    n_safe = 0
    for row in data:
        report = [int(nr) for nr in row.split()]
        if is_safe(report):
            n_safe += 1
        elif dampen:
            if is_safe_dampened(report):
                n_safe += 1
    return n_safe


print("Part 1:", solve(data))
print("Part 2:", solve(data, True))
