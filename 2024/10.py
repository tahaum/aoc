from collections import defaultdict

from utils.io import read_input

data_path = "data/input_10.txt"
GRID = read_input(data_path).splitlines()
X, Y = len(GRID[0]), len(GRID)
for y in range(Y):
    GRID[y] = [int(c) for c in list(GRID[y])]
DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))


def step(x_org, y_org, x, y, val, trailheads) -> None:
    for dx, dy in DIRS:
        if not (0 <= x + dx < X and 0 <= y + dy < Y):
            continue
        dir_val = GRID[y + dy][x + dx]
        if val == 8 and dir_val == 9:
            trailheads[(x_org, y_org)].append((x + dx, y + dy))
            continue
        elif dir_val == (val + 1):
            step(x_org, y_org, x + dx, y + dy, dir_val, trailheads)


def solve() -> int:
    trailheads = defaultdict(list)
    for y in range(Y):
        for x in range(X):
            if GRID[y][x] == 0:
                step(x, y, x, y, 0, trailheads)
    return sum([len(set(v)) for _, v in trailheads.items()]), sum(
        [len(v) for _, v in trailheads.items()]
    )


p1, p2 = solve()
print("Part 1:", p1)
print("Part 2:", p2)
