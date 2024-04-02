with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

def check_in_bounds(row, col, num_rows, num_cols) -> bool:
    if row >= num_rows or row < 0 or col >= num_cols or col < 0:
        return False
    return True

def evaluate_splitters(tile, direction) -> list:
    if tile == '.':
        return [direction]
    elif tile == "/":
        if direction == 'r':
            return ['u']
        elif direction == 'l':
            return ['d']
        elif direction == 'd':
            return ['l']
        else:
            return ['r']
    elif tile == '\\':
        if direction == 'r':
            return['d']
        elif direction == 'l':
            return ['u']
        elif direction == 'd':
            return ['r']
        else:
            return ['l']
    elif tile == "|":
        if direction == 'r' or direction == 'l':
            return ['u', 'd']
        else:
            return [direction]
    elif tile == "-":
        if direction == 'r' or direction == 'l':
            return [direction]
        else:
            return ['l', 'r']


def part_1():
    queue = [(0, 0, 'r')]
    grid = [list(line) for line in lines]
    num_rows = len(grid)
    num_cols = len(grid[0])
    seen = set()
    energized = [[False for c in range(num_cols)] for r in range(num_rows)]

    while queue:
        row, col, direction = queue.pop(0)
        if (row, col, direction) in seen:
            continue
        seen.add((row, col, direction))
        energized[row][col] = True
        next_row, next_col = row, col
        next_directions = evaluate_splitters(grid[row][col], direction)

        for direction in next_directions:
            if direction == 'r':
                next_col += 1
            if direction == 'l':
                next_col -= 1
            if direction == 'u':
                next_row -= 1
            if direction == 'd':
                next_row += 1

            if check_in_bounds(next_row, next_col, num_rows, num_cols):
                queue.append((next_row, next_col, direction))

    res = 0

    for row in range(num_rows):
        for col in range(num_cols):
            if energized[row][col]:
                res += 1
    return res


def bfs(grid, queue, num_rows, num_cols):
    seen = set()
    energized = [[False for c in range(num_cols)] for r in range(num_rows)]

    while queue:
        row, col, direction = queue.pop(0)
        if (row, col, direction) in seen:
            continue
        seen.add((row, col, direction))
        energized[row][col] = True
        next_row, next_col = row, col
        next_directions = evaluate_splitters(grid[row][col], direction)

        for direction in next_directions:
            if direction == 'r':
                next_col += 1
            if direction == 'l':
                next_col -= 1
            if direction == 'u':
                next_row -= 1
            if direction == 'd':
                next_row += 1

            if check_in_bounds(next_row, next_col, num_rows, num_cols):
                queue.append((next_row, next_col, direction))

    res = 0

    for row in range(num_rows):
        for col in range(num_cols):
            if energized[row][col]:
                res += 1
    return res



def part_2():
    grid = [list(line) for line in lines]
    num_rows = len(grid)
    num_cols = len(grid[0])
    max_energized = 0
    for row in range(num_rows):
        max_energized = max(max_energized, bfs(grid, [(row, 0, 'r')], num_rows, num_cols))
        max_energized = max(max_energized, bfs(grid, [(row, num_cols - 1, 'l')], num_rows, num_cols))
    for col in range(num_cols):
        max_energized = max(max_energized, bfs(grid, [(0, col, 'd')], num_rows, num_cols))
        max_energized = max(max_energized, bfs(grid, [(num_rows - 1, col, 'u')], num_rows, num_cols))


    return max_energized
print(part_2())
