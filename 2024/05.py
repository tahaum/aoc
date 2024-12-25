from utils.io import read_input

data_path = "data/input_05.txt"
data = read_input(data_path).splitlines()


def parse_input(data: list) -> tuple:
    rules, updates = [], []
    for row in data:
        if "|" in row:
            rules.append([int(i) for i in row.split("|")])
        elif len(row) > 0:
            updates.append([int(i) for i in row.split(",")])
    return rules, updates


def split_updates(rules: list, updates: list) -> tuple:
    correct, incorrect = [], []
    for u in updates:
        (correct if correct_update(u, rules) else incorrect).append(u)
    return correct, incorrect


def correct_update(update: list, rules: list) -> bool:
    for r in rules:
        if not correct_according_to_rule(update, r):
            return False
    return True


def correct_according_to_rule(update: list, rule: list) -> bool:
    if (rule[0] in update) and (rule[1] in update):
        if not (update.index(rule[0]) < update.index(rule[1])):
            return False
    return True


def apply_rule(update: list, rule: list) -> None:
    idx = update.index(rule[1])
    update.remove(rule[0])
    update.insert(idx, rule[0])


def solve_p1(data: list) -> int:
    rules, updates = parse_input(data)
    correct, _ = split_updates(rules, updates)
    return sum([c[len(c) // 2] for c in correct])


def solve_p2(data: list) -> int:
    rules, updates = parse_input(data)
    _, incorrect = split_updates(rules, updates)
    for inc in incorrect:
        while not correct_update(inc, rules):
            for r in rules:
                if not correct_according_to_rule(inc, r):
                    apply_rule(inc, r)
    return sum([c[len(c) // 2] for c in incorrect])


print("Part 1:", solve_p1(data))
print("Part 2:", solve_p2(data))
