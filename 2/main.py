with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

# red: 12
# green: 13
# blue: 14

def parse_line(line: str) -> dict:
    id = int(line.split()[1][:-1])

    res = {"id": id, "groups": []}

    groups = line.split(":")[1].split(";")
    for group in groups:
        group_map = {}
        for elem in group.split(','):
            val = int(elem.split()[0])
            color = elem.split()[1]
            group_map[color] = val
        res["groups"].append(group_map)
    return res


MAX_VALS = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def validate_line(line: dict):
    for group in line['groups']:
        for key, val in group.items():
            if val > MAX_VALS[key]:
                return False
    return True

def get_minimums(line: dict):
    res = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for group in line['groups']:
        for key, val in group.items():
            res[key] = max(res[key], val)

    return res
    

def part_1():
    res = 0

    for line in lines:
        m = parse_line(line)
        id = m['id']
        if validate_line(m):
            res += id
    return res

def part_2():
    res = 0
    for line in lines:
        m = parse_line(line)
        min_colors = get_minimums(m)
        power = min_colors['red'] * min_colors['blue'] * min_colors['green']
        res += power
    return res

print(part_2())