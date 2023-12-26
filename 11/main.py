with open('input.txt') as file:
    lines = [list(line.rstrip()) for line in file]

def expand_map(grid):
    rows_to_expand = set()
    cols_to_expand = set()

    num_rows = len(grid)
    num_cols = len(grid[0])

    for row_num in range(num_rows):
        if not any(c == "#" for c in grid[row_num]):
            rows_to_expand.add(row_num)

    for col_num in range(num_cols):
        should_expand = True
        for row_num in range(len(grid)):
            if grid[row_num][col_num] == "#":
                should_expand = False
        if should_expand:
            cols_to_expand.add(col_num)


    new_grid = []
    for row_num in range(num_rows):
        new_grid.append(grid[row_num].copy())
        if row_num in rows_to_expand:
            new_grid.append(grid[row_num].copy())

    col_diff = 0

    for col_num in range(num_cols):
        if col_num in cols_to_expand:
            for row in new_grid:
                row.insert(col_num + col_diff, ".")
            col_diff += 1

    return new_grid

def get_galaxy_coords(grid):
    coords = []
    for row_num in range(len(grid)):
        for col_num in range(len(grid[0])):
            if grid[row_num][col_num] == "#":
               coords.append((row_num, col_num))

    return coords


def get_distance(row1, col1, row2, col2):
    return abs(row2 - row1) + abs(col2 - col1)


def part_1():
    expanded_map = expand_map(lines)
    for row in expanded_map:
        print(row)

    galaxy_coords = get_galaxy_coords(expanded_map)
    min_distances = []
    for galaxy1 in galaxy_coords:
        for galaxy2 in galaxy_coords:
            if galaxy1 != galaxy2:
                min_distance = get_distance(galaxy1[0], galaxy1[1], galaxy2[0], galaxy2[1])
                print(f"distance from {galaxy1} to {galaxy2} = {min_distance}")
                min_distances.append(min_distance)

    print(sum(min_distances)//2)


def get_expansions(grid):
    rows_to_expand = set()
    cols_to_expand = set()

    num_rows = len(grid)
    num_cols = len(grid[0])

    for row_num in range(num_rows):
        if not any(c == "#" for c in grid[row_num]):
            rows_to_expand.add(row_num)

    for col_num in range(num_cols):
        should_expand = True
        for row_num in range(len(grid)):
            if grid[row_num][col_num] == "#":
                should_expand = False
        if should_expand:
            cols_to_expand.add(col_num)

    return((rows_to_expand, cols_to_expand))


def get_distance_across_expansions(row1, col1, row2, col2, rows_to_expand, cols_to_expand, factor):
    start_y = min(row1, row2)
    end_y = max(row1, row2)
    dy = 0
    for y in range(start_y, end_y):
        if y in rows_to_expand:
            dy += factor
        else:
            dy += 1

    start_x = min(col1, col2)
    end_x = max(col1, col2)
    dx = 0
    for x in range(start_x, end_x):
        if x in cols_to_expand:
            dx += factor
        else:
            dx += 1

    return dx + dy

def part_2():
    galaxy_coords = get_galaxy_coords(lines)
    row_expansions, col_expansions = get_expansions(lines)

    distances = []

    for galaxy1 in galaxy_coords:
        for galaxy2 in galaxy_coords:
            if galaxy1 != galaxy2:
                distances.append(get_distance_across_expansions(galaxy1[0], galaxy1[1], galaxy2[0], galaxy2[1], row_expansions, col_expansions, 1_000_000))

    print(sum(distances) // 2)


part_2()
