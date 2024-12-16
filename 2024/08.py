from utils.io import read_input

data_path = "data/input_08.txt"
GRID = read_input(data_path).splitlines()
X, Y = len(GRID[0]), len(GRID)


def check_for_antinodes_at_pos(x: int, y: int, antinodes: set, part: int) -> set:
    char = GRID[y][x]
    for y_, row in enumerate(GRID):
        for x_, char_ in enumerate(row):
            if (x, y) != (x_, y_) and char == char_ and char != ".":
                dx, dy = x - x_, y - y_
                if part == 2:
                    antinodes.add((x, y))
                    antinodes.add((x_, y_))
                antinodes = step(x, y, dx, dy, antinodes, part)
                antinodes = step(x_, y_, -dx, -dy, antinodes, part)
    return antinodes


def step(x: int, y: int, dx: int, dy: int, antinodes: set, part: int) -> set:
    step = 1
    max_steps = 1 if part == 1 else 999
    while (
        0 <= (x + (dx * step)) < X and 0 <= (y + (dy * step)) < Y
    ) and step <= max_steps:
        antinodes.add((x + (dx * step), y + (dy * step)))
        step += 1
    return antinodes


def solve(part: int) -> int:
    antinodes = set()
    for x in range(X):
        for y in range(Y):
            antinodes = check_for_antinodes_at_pos(x, y, antinodes, part)
    return len(antinodes)


print("Part 1:", solve(1))
print("Part 2:", solve(2))
