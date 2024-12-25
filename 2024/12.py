from utils.io import read_input

data_path = "data/input_12.txt"
GRID = read_input(data_path).splitlines()
X, Y = len(GRID[0]), len(GRID)
DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))


def step(queue, visited):
    size, peri = 1, 0
    while len(queue) > 0:
        x, y = queue.pop()
        char = GRID[y][x]
        neighbors = 0
        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy
            if (not (0 <= nx < X and 0 <= ny < Y)) or GRID[ny][nx] != char:
                peri += 1
            elif (nx, ny) not in visited:
                size += 1
                neighbors += 1
                visited.add((nx, ny))
                queue.append((nx, ny))

    return size, peri, visited


def solve_p1():
    visited = set()
    regions = list()
    for x in range(X):
        for y in range(Y):
            if (x, y) not in visited:
                visited.add((x, y))
                size, peri, visited = step([(x, y)], visited)
                regions.append((size, peri))
    return sum([size * peri for size, peri in regions])


print("Part 1:", solve_p1())
