from math import inf
import heapq

with open('test_input.txt') as file:
    lines = [line.rstrip() for line in file]


def check_in_bounds(row, col, num_rows, num_cols):
    if row >= 0 and row < num_rows and col >= 0 and col < num_cols:
        return True
    return False


def part_1():
    grid = [list(line) for line in lines]
    num_rows = len(grid)
    num_cols = len(grid[0])

    # elements = (cost, row, col, direction, num_steps)
    priority_queue = [
        (0, 0, 0, 'd', 0),
        (0, 0, 0, 'r', 0)
    ]
    seen = set()

    directions = [('r', 0, 1), ('l', 0, -1), ('u', -1, 0), ('d', 1, 0)]
    while priority_queue:
        heat_loss, row, col, direction, num_steps = heapq.heappop(priority_queue)
        print(f"{heat_loss} {row} {col} {direction} {num_steps}")
        if row == num_rows - 1 and col == num_cols - 1:
            return heat_loss

        if (row, col, num_steps) in seen:
            continue
        seen.add((row, col, num_steps))
        for next_direction, d_row, d_col in directions:
            if direction == 'l' and next_direction == 'r':
                continue
            if direction == 'r' and next_direction == 'l':
                continue
            if direction == 'u' and next_direction == 'd':
                continue
            if direction == 'd' and next_direction == 'u':
                continue

            next_row = row + d_row
            next_col = col + d_col
            if check_in_bounds(next_row, next_col, num_rows, num_cols):
                if direction == next_direction and num_steps < 3:
                    heapq.heappush(priority_queue, (heat_loss + int(grid[next_row][next_col]), next_row, next_col, next_direction, num_steps + 1))
                else:
                    heapq.heappush(priority_queue, (heat_loss + int(grid[next_row][next_col]), next_row, next_col, next_direction, 1))

    return -1

print(part_1())
