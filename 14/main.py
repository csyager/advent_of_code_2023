with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def roll_north(grid, rows, cols):
    rows = len(grid)
    cols = len(grid[0])

    for col in range(cols):
        landing_row = 0
        for row in range(rows):
            if grid[row][col] == "#":
                landing_row = row + 1
            elif grid[row][col] == "O":
                grid[row][col] = "."
                grid[landing_row][col] = "O"
                landing_row += 1
    return grid


def roll_south(grid, rows, cols):

    for col in range(cols):
        landing_row = rows - 1
        for row in range(rows-1, -1, -1):
            if grid[row][col] == "#":
                landing_row = row - 1
            elif grid[row][col] == "O":
                grid[row][col] = "."
                grid[landing_row][col] = "O"
                landing_row -= 1
    return grid


def roll_east(grid, rows, cols):
    for row in range(rows):
        landing_col = cols - 1
        for col in range(cols-1, -1, -1):
            if grid[row][col] == "#":
                landing_col = col - 1
            elif grid[row][col] == "O":
                grid[row][col] = "."
                grid[row][landing_col] = "O"
                landing_col -= 1
    return grid


def roll_west(grid, rows, cols):
    for row in range(rows):
        landing_col = 0
        for col in range(cols):
            if grid[row][col] == "#":
                landing_col = col + 1
            elif grid[row][col] == "O":
                grid[row][col] = "."
                grid[row][landing_col] = "O"
                landing_col += 1
    return grid



def calculate_load(grid):
    rows = len(grid)
    cols = len(grid[0])

    load = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "O":
                load += (rows - row)
    return load


class CycleDetected(Exception):
    def __init__(self, last_seen_cycle, current_cycle):
        self.last_seen_cycle = last_seen_cycle
        self.current_cycle = current_cycle
        pass


def cycle(grid, seen_grids, current_cycle):
    rows = len(grid)
    cols = len(grid[0])

    grid = roll_north(grid, rows, cols)
    grid = roll_west(grid, rows, cols)
    grid = roll_south(grid, rows, cols)
    grid = roll_east(grid, rows, cols)

    load = calculate_load(grid)
    print(f"{current_cycle}: {load}")
    if str(grid) in seen_grids:
        print(f"cycle detected! This grid was seen at {seen_grids[str(grid)]}, current cycle is {current_cycle}")
        raise CycleDetected(seen_grids[str(grid)], current_cycle)

    seen_grids[str(grid)] = current_cycle
    return grid


def part_1():
    grid = []
    for line in lines:
        grid.append(list(line))
    grid = roll_north(grid)

    for line in grid:
        print(''.join(line))

    print(calculate_load(grid))

def part_2():
    seen_grids = {}
    grid = []
    for line in lines:
        grid.append(list(line))

    for i in range(1000000000):
        try:
            grid = cycle(grid, seen_grids, i)
        except CycleDetected as e:
            cycle_length = e.current_cycle - e.last_seen_cycle
            target_position_in_cycle = (1000000000 - e.last_seen_cycle) % cycle_length
            print(f"Cycle length = {cycle_length}.  Result of 1000000000th cycle will equal result of cycle {e.last_seen_cycle + target_position_in_cycle - 1}")
            break



    for line in grid:
        print(''.join(line))


part_2()
