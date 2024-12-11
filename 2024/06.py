from utils.io import read_input

data_path = "data/input_06.txt"
GRID = [list(row) for row in read_input(data_path).splitlines()]
X, Y = len(GRID[0]), len(GRID)


def find_start_pos() -> tuple:
    char = "^"
    for y, row in enumerate(GRID):
        if char in row:
            return row.index(char), y


def rotate(dir: tuple) -> tuple:
    return {(0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1)}[dir]


def within(x, y) -> bool:
    return 0 <= x < X and 0 <= y < Y


def solve_p1() -> int:
    visited = []
    dx, dy = (0, -1)
    x, y = find_start_pos()
    while within(x, y):
        if (x, y) not in visited:
            visited.append((x, y))
        if within(x + dx, y + dy) and GRID[y + dy][x + dx] == "#":
            while GRID[y + dy][x + dx] == "#":
                dx, dy = rotate((dx, dy))
        x += dx
        y += dy
    return len(visited), visited


def solve_p2() -> int:
    _, original_route = solve_p1()
    loops = 0
    for pos in original_route[1:]:
        x, y = original_route[0]
        x_obs, y_obs = (int(i) for i in pos)
        visited = set()
        dx, dy = (0, -1)
        while within(x, y):
            visited.add((x, y, dx, dy))
            if within(x + dx, y + dy) and (
                GRID[y + dy][x + dx] == "#" or (x + dx, y + dy) == (x_obs, y_obs)
            ):
                while GRID[y + dy][x + dx] == "#" or (x + dx, y + dy) == (x_obs, y_obs):
                    dx, dy = rotate((dx, dy))
            x += dx
            y += dy
            if (x, y, dx, dy) in visited:
                loops += 1
                break
    return loops


print("Part 1:", solve_p1()[0])
print("Part 2:", solve_p2())
