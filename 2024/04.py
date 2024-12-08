from copy import copy

from utils.io import read_input

data_path = "data/input_04.txt"
data = read_input(data_path).splitlines()

L, R, U, D = (-1, 0), (1, 0), (0, -1), (0, 1)
LU, RU, LD, RD = (-1, -1), (1, -1), (-1, 1), (1, 1)
DIRS = [L, R, U, D, LU, RU, LD, RD]


def within(x, y, X, Y) -> bool:
    return (0 <= x < X) and (0 <= y < Y)


def solve_p1(data: list) -> int:
    CHARS = "XMAS"
    X, Y = len(data[0]), len(data)
    n_words = 0
    for y, row in enumerate(data):
        for x, char in enumerate(row):
            if char == CHARS[0]:
                for dir in DIRS:
                    x_, y_ = copy(x), copy(y)
                    for idx, search_char in enumerate(CHARS[1:]):
                        if y == 9:
                            pass
                        x_ += dir[0]
                        y_ += dir[1]
                        if within(x_, y_, X, Y):
                            char_ = data[y_][x_]
                            if not char_ == search_char:
                                break
                            if idx == 2:
                                n_words += 1
                                break
                        else:
                            break

    return n_words


def solve_p2(data: list) -> int:
    X, Y = len(data[0]), len(data)
    n_words = 0
    for y, row in enumerate(data):
        for x, char in enumerate(row):
            if char == "A":
                success = True
                for dirs in [(LU, RD), (LD, RU)]:
                    x_, y_ = x + dirs[0][0], y + dirs[0][1]
                    x_opp, y_opp = x + dirs[1][0], y + dirs[1][1]
                    if within(x_, y_, X, Y) and within(x_opp, y_opp, X, Y):
                        char_ = data[y_][x_]
                        char_opp = data[y_opp][x_opp]
                        if not (
                            (char_ == "M" and char_opp == "S")
                            or (char_ == "S" and char_opp == "M")
                        ):
                            success = False
                            break
                    else:
                        success = False
                        break
                if success:
                    n_words += 1

    return n_words


print("Part 1:", solve_p1(data))
print("Part 2:", solve_p2(data))
