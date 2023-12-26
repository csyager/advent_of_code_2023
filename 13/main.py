with open('test_input.txt') as file:
    lines = [line.rstrip() for line in file]

grids = []
current_grid = []
for line in lines:
    if line == "":
        grids.append(current_grid)
        current_grid = []
    else:
        current_grid.append(line)

grids.append(current_grid)


def find_vertical_mirror(grid, allowed_smudges=0):
    cols = len(grid[0])
    rows = len(grid)
    possible_reflections = [True for _ in range(cols - 1)]
    smudges_for_col = [0 for _ in range(cols - 1)]
    for row in range(rows):
        line = grid[row]
        for col in range(cols - 1):
            left = col
            if possible_reflections[left]:
                right = left + 1
                while left >= 0 and right < cols:
                    if line[left] != line[right]:
                        if smudges_for_col[col] == allowed_smudges:
                            possible_reflections[col] = False
                            break
                        else:
                            smudges_for_col[col] += 1
                    left -= 1
                    right += 1
    for col in range(len(possible_reflections)):
        if possible_reflections[col] and smudges_for_col[col] == allowed_smudges:
            return col + 1
    return -1


def find_horizontal_mirror(grid, allowed_smudges=0):
    cols = len(grid[0])
    rows = len(grid)
    possible_reflections = [True for _ in range(rows - 1)]
    smudges_for_row = [0 for _ in range(rows - 1)]
    for col in range(cols):
        for row in range(rows - 1):
            top = row
            if possible_reflections[top]:
                bottom = top + 1
                while top >= 0 and bottom < rows:
                    if grid[top][col] != grid[bottom][col]:
                        if smudges_for_row[row] == allowed_smudges:
                            possible_reflections[row] = False
                            break
                        else:
                            smudges_for_row[row] += 1
                    top -= 1
                    bottom += 1
    for row in range(len(possible_reflections)):
        if possible_reflections[row] and smudges_for_row[row] == allowed_smudges:
            return row + 1
    return -1

def part_1():
    cols_before = 0
    rows_before = 0

    for grid in grids:
        vertical_mirror = find_vertical_mirror(grid)
        horizontal_mirror = find_horizontal_mirror(grid)

        if vertical_mirror != -1:
            cols_before += vertical_mirror
        if horizontal_mirror != -1:
            rows_before += horizontal_mirror * 100
    print(cols_before + rows_before)


def part_2():
    cols_before = 0
    rows_before = 0

    for grid in grids:
        vertical_mirror = find_vertical_mirror(grid, 1)
        horizontal_mirror = find_horizontal_mirror(grid, 1)

        if vertical_mirror != -1:
            cols_before += vertical_mirror
        if horizontal_mirror != -1:
            rows_before += horizontal_mirror * 100

    print(cols_before + rows_before)

part_1()
part_2()
