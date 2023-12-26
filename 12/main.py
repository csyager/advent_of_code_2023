with open('test_input.txt') as file:
    lines = [line.rstrip() for line in file]

DP = {}
def get_possible_arrangements_from_idx(dots, blocks, dots_idx, blocks_idx, group_len):
    key = (dots_idx, blocks_idx, group_len)
    if key in DP:
        return DP[key]
    # if we're at the end of the input...
    if dots_idx == len(dots):
        # ... and we've been through all blocks and the current block length is 0
        if blocks_idx == len(blocks) and group_len == 0:
            return 1
        # ... and we're on the last block and the current block length is equal to the last valid block length
        elif blocks_idx == len(blocks) - 1 and blocks[blocks_idx] == group_len:
            return 1
        # ... and we have an invalid choice of blocks up to this point
        else:
            return 0

    ans = 0

    if dots[dots_idx] == "." or dots[dots_idx] == '?':
        # not currently in a block, so increment dots idx
        if group_len == 0:
            ans += get_possible_arrangements_from_idx(dots, blocks, dots_idx + 1, blocks_idx, 0)
        # currently in a block, haven't been through all blocks, but the current block satisfies the condition
        elif group_len > 0 and blocks_idx < len(blocks) and blocks[blocks_idx] == group_len:
            ans += get_possible_arrangements_from_idx(dots, blocks, dots_idx + 1, blocks_idx + 1, 0)

                if dots[dots_idx] == '#' or dots[dots_idx] == '?':
        ans += get_possible_arrangements_from_idx(dots, blocks, dots_idx + 1, blocks_idx, group_len + 1)

    DP[key] = ans
    return ans 

def part_1():
    possible_arrangements = 0
    for line in lines:
        dots, blocks = line.split()
        blocks = [int(x) for x in blocks.split(',')]
        possible_arrangements_for_line = get_possible_arrangements_from_idx(dots, blocks, 0, 0, 0)
        print(f"possible arrangements for line {line} = {possible_arrangements_for_line}")
        possible_arrangements += possible_arrangements_for_line

    return possible_arrangements

print(part_1())
