from utils.io import read_input

data_path = "data/input_09.txt"
data = list(read_input(data_path).strip())

FREE = -1


def create_blocks(data: list) -> list:
    blocks = list()
    block_id = 0
    for idx, char in enumerate(data):
        if idx % 2 == 0:
            blocks.extend([block_id] * int(char))
            block_id += 1
        else:
            blocks.extend([FREE] * int(char))
    return blocks


def move_files_split(blocks: list) -> list:
    L = len(blocks)
    n_free = blocks.count(FREE)
    blocks_reversed = list(reversed(blocks))
    while not compact(blocks_reversed, n_free):
        block_id = get_end_block_id(blocks_reversed)
        idx_fetch = blocks_reversed.index(block_id)
        idx_put = blocks.index(FREE)
        blocks[L - idx_fetch - 1] = FREE
        blocks[idx_put] = block_id
        blocks_reversed = list(reversed(blocks))
    return blocks


def get_consecutive_free(blocks: list, index: int) -> int:
    try:
        for i in range(index + 1, 99999):
            if blocks[i] != FREE:
                return i - index
        raise ValueError("No free space found!")
    except IndexError:
        return 0


def get_first_consective_free_of_length(blocks: list, min_length: int):
    for i, b in enumerate(blocks):
        if b == FREE:
            length = get_consecutive_free(blocks, i)
            if length >= min_length:
                return i, length
    return None, None


def move_files_whole(blocks: list) -> list:
    L = len(blocks)
    n_free = blocks.count(FREE)
    blocks_reversed = list(reversed(blocks))
    block_id = get_end_block_id(blocks_reversed)
    while block_id > 0 and not compact(blocks_reversed, n_free):
        idx_fetch = blocks_reversed.index(block_id)
        file_size = blocks.count(block_id)
        idx_put, free_size = get_first_consective_free_of_length(blocks, file_size)
        if (
            idx_put
            and (idx_put < (L - idx_fetch - file_size))
            and (free_size >= file_size)
        ):
            blocks[idx_put : idx_put + file_size] = [block_id] * file_size
            blocks[L - idx_fetch - file_size : L - idx_fetch] = [FREE] * file_size
            blocks_reversed = list(reversed(blocks))
        block_id -= 1
    return blocks


def compact(blocks_reversed: list, n_free: int) -> bool:
    streak = 0
    for i in blocks_reversed:
        if i == FREE:
            streak += 1
        else:
            break
    if streak == n_free:
        return True
    return False


def get_end_block_id(blocks_reversed: list) -> int:
    for i in blocks_reversed:
        if i != FREE:
            return i
    raise ValueError("No block ID found!")


def checksum(blocks: list) -> int:
    return sum([idx * b if b > 0 else 0 for idx, b in enumerate(blocks)])


def solve(data: list, whole_files: bool = False) -> int:
    blocks = create_blocks(data)
    if whole_files:
        blocks = move_files_whole(blocks)
    else:
        blocks = move_files_split(blocks)
    return checksum(blocks)


print("Part 1:", solve(data))
print("Part 2:", solve(data, True))
