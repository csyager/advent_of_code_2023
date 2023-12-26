with open('test_input.txt') as file:
    lines = [line.rstrip() for line in file ]

def is_connected(direction, pipe):
    if pipe == "L":
        return direction == "north" or direction == "east"
    if pipe == "J":
        return direction == "west" or direction == "north"
    if pipe == "7":
        return direction == "west" or direction == "south"
    if pipe == "F":
        return direction == "south" or direction == "east"

    if pipe == "-":
        return direction == "west" or direction == "east"
    if pipe == "|":
        return direction == "north" or direction == "south"

    return False


def check_bounds(row, col, rows, cols):
    if row >= 0 and row < rows and col >= 0 and col < cols:
        return True
    else:
        return False

def get_starting_coords(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "S":
                return (row, col)

def part_1():
    max_distance = 0
    rows = len(lines)
    cols = len(lines[0])
    distance = [[0 for i in range(cols)] for j in range(rows)]

    directions = {
        'south': (-1, 0),
        'north': (1, 0),
        'west': (0, 1),
        'east': (0, -1)
    }

    starting_coords = get_starting_coords(lines)

    queue = [(starting_coords[0], starting_coords[1], 0)]
    while queue:
        row, col, steps = queue.pop(0)
        print(f"at {row}, {col}, steps = {steps}")
        distance[row][col] = steps
        max_distance = max(max_distance, steps)
        for direction in directions.keys():
            dy, dx = directions[direction]
            next_row = row + dy
            next_col = col + dx
            if check_bounds(next_row, next_col, rows, cols) and is_connected(direction, lines[next_row][next_col]) and not distance[next_row][next_col]:
                queue.append((next_row, next_col, steps + 1))


    for row in distance:
        print(row)

    print(max_distance)


def part_2():
    rows = len(lines)
    cols = len(lines[0])
    grid = []
    for line in lines:
        row = []
        for char in line:
            row.append(char)
        grid.append(row)

    row, col = get_starting_coords(grid)
    directions = {
        'south': (-1, 0),
        'north': (1, 0),
        'west': (0, 1),
        'east': (0, -1)
    }

    
    connected = {'north': False, 'south': False, 'east': False, 'west': False}

    for direction in directions.keys():
        dy, dx = directions[direction]
        next_row, next_col = row + dy, col + dx
        if check_bounds(next_row, next_col, rows, cols) and is_connected(direction, grid[next_row][next_col]):
            connected[direction] = True

    if connected['south'] and connected['west']:
        grid[row][col] = 'L'
    if connected['south'] and connected['east']:
        grid[row][col] = 'J'
    if connected['north'] and connected['east']:
        grid[row][col] = '7'
    if connected['north'] and connected['west']:
        grid[row][col] = 'F'
    if connected['south'] and connected['north']:
        grid[row][col] = "|"
    if connected['east'] and connected['west']:
        grid[row][col] = "-"
    
    part_of_loop = [[False for i in range(cols)] for j in range(rows)]

    queue = [(row, col)]
    while queue:
        row, col = queue.pop(0)
        part_of_loop[row][col] = True
        print(f"at {row}, {col}")
        for direction in directions.keys():
            dy, dx = directions[direction]
            next_row = row + dy
            next_col = col + dx
            if check_bounds(next_row, next_col, rows, cols) and is_connected(direction, grid[next_row][next_col]) and not part_of_loop[next_row][next_col]:
                queue.append((next_row, next_col))



    count = 0
    for i in range(rows):
        in_loop = False
        for j in range(cols):
            if grid[i][j] == "|" or grid[i][j] == "L" or grid[i][j] == "J":
                in_loop = not in_loop
            if in_loop and not part_of_loop[i][j]:
                grid[i][j] = "I"
                count += 1
    for row in grid:
        for char in row:
            print(char, end="")
        print("")


    for row in part_of_loop:
        for b in row:
            if b:
                print('T', end="")
            else:
                print('F', end="")
        print("")

    print(count)

part_2()
