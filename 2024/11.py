from collections import defaultdict
from copy import deepcopy
from math import log10

from utils.io import read_input

data_path = "data/input_11.txt"
data = [int(s) for s in read_input(data_path).split()]


def digits(x) -> int:
    return int(log10(x)) + 1


def solve_naively(data: list, blinks: int) -> int:
    stones = deepcopy(data)
    for _ in range(blinks):
        idx = 0
        while idx < len(stones):
            stone = stones[idx]
            if stone == 0:
                stones[idx] = 1
            elif ((n_digits := digits(stone)) % 2) == 0:
                half = n_digits // 2
                stone_str = str(stone)
                stones[idx] = int(stone_str[:half])
                stones.insert(idx + 1, int(stone_str[half:]))
                idx += 1
            else:
                stones[idx] = stones[idx] * 2024
            idx += 1
    return len(stones)


def solve(data: list, blinks: int) -> int:
    stones = defaultdict(int)
    for stone in data:
        stones[stone] += 1

    for _ in range(blinks):
        new_stones = defaultdict(int)
        for stone, count_ in stones.items():
            if stone == 0:
                new_stones[1] += count_
            elif ((n_digits := digits(stone)) % 2) == 0:
                half = n_digits // 2
                stone_str = str(stone)
                new_stones[int(stone_str[:half])] += count_
                new_stones[int(stone_str[half:])] += count_
            else:
                new_stones[stone * 2024] += count_
        stones = new_stones
    return sum([v for v in stones.values()])


print("Part 1:", solve_naively(data, 25))
print("Part 2:", solve(data, 75))
