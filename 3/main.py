with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

def next_to_symbol(row, col, matrix):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dx, dy in directions:
        next_row = row + dx
        next_col = col + dy
        # check bounds
        if next_row >= 0 and next_row < len(matrix) and next_col >= 0 and next_col < len(matrix[0]):
            if not matrix[next_row][next_col].isdigit() and matrix[next_row][next_col] != ".":
                return True
    return False

def get_integer_at_index(row, col, matrix, visited):
    builder = []
    while True:
        if col - 1 >= 0 and matrix[row][col - 1].isdigit():
            col -= 1
        else:
            break
    while col < len(matrix[0]) and matrix[row][col].isdigit():
        visited.append((row, col))
        builder.append(matrix[row][col])
        col += 1
    return int(''.join(builder))


def get_adjacent_vals(row, col, matrix):
    visited = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    adjacent_vals = []
    for dx, dy in directions:
        next_row = row + dy
        next_col = col + dx
        if next_row >= 0 and next_row < len(matrix) and next_col >= 0 and next_col < len(matrix[0]):
            if matrix[next_row][next_col].isdigit() and (next_row, next_col) not in visited:
                print(f"getting adjacents at {next_row}, {next_col}, visited: {visited}")
                adjacent_vals.append(get_integer_at_index(next_row, next_col, matrix, visited))
    print(f"adjacents at {row}, {col} = {adjacent_vals}")
    return adjacent_vals

def part_1():
    row = 0
    num_rows = len(lines)
    num_cols = len(lines[0])
    s = 0
    while row < num_rows:
        col = 0
        while col < num_cols:
            if lines[row][col].isdigit():
                builder = []
                valid = False
                while True:
                    builder.append(lines[row][col])
                    if next_to_symbol(row, col, lines):
                        valid = True
                    if col + 1 < num_cols and lines[row][col + 1].isdigit():
                        col += 1
                    else:
                        break
                if valid:
                    print(f"adding {''.join(builder)}")
                    s += int(''.join(builder))
            col += 1
        row += 1
    return s


def part_2():
    s = 0
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            if lines[row][col] == "*":
                adjacent_vals = get_adjacent_vals(row, col, lines)
                if len(adjacent_vals) == 2:
                    print(f"gears at {row}, {col}: {adjacent_vals}")
                    s += adjacent_vals[0] * adjacent_vals[1]
    return s
    

print(part_2())