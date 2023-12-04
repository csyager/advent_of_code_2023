with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

def parse_line(line: str):
    res = {}
    id = int(line.split(":")[0].split()[1])
    winning_numbers = line.split(":")[1].split("|")[0].split()
    your_numbers = line.split(":")[1].split("|")[1].split()
    res['id'] = id
    res['winning_numbers'] = winning_numbers
    res['your_numbers'] = your_numbers
    return res


def part_1():
    s = 0
    for line in lines:
        m = parse_line(line)
        num_winning_nums = 0
        winning_nums = []
        for number in m['your_numbers']:
            if number in m['winning_numbers']:
                winning_nums.append(number)
                num_winning_nums += 1
        if num_winning_nums > 0:
            s += 2 ** (num_winning_nums - 1)
        print(f"card scores {s} points")
        print(winning_nums)
    print(s)
    return s


def build_map(lines: list):
    res = {}
    for line in lines:
        id = int(line.split(":")[0].split()[1])
        winning_numbers = line.split(":")[1].split("|")[0].split()
        your_numbers = line.split(":")[1].split("|")[1].split()
        res[id] = {
            'winning_numbers': winning_numbers,
            'your_numbers': your_numbers
        }
    return res

def get_matches_in_line(line: dict):
    num_winners = 0
    for number in line['your_numbers']:
        if number in line['winning_numbers']:
            num_winners += 1
    return num_winners

def part_2():
    m = build_map(lines)
    copies = {id: 1 for id in m.keys()}
    for id, numbers in m.items():
        winners = get_matches_in_line(numbers)
        for i in range(1, winners + 1):
            copies[id + i] += copies[id]
    print(copies)
    print(sum(copies.values()))
    return sum(copies.values())

part_2()