initialization_seq = []

with open('test_input.txt') as file:
    lines = [line.rstrip() for line in file]
    for line in lines:
        instructions = line.split(',')
        initialization_seq += instructions

print(initialization_seq)

def hash_string(s):
    current_val = 0
    for c in s:
        current_val += ord(c)
        current_val *= 17
        current_val %= 256

    return current_val


def part_1():
    res = 0
    for s in initialization_seq:
        res += hash_string(s)

    return res


def get_focusing_power(hashmap):
    res = 0
    for box_idx in range(len(hashmap)):
        slot = 1
        for i in range(len(hashmap[box_idx])):
            if hashmap[box_idx][i] != None:
                key, value = hashmap[box_idx][i]
                power = (box_idx + 1) * slot * value
                print(f"{key}: {box_idx + 1} * {slot} * {value} = {power}")
                slot += 1
                res += power

    return res

def add_to_box(box, label, value):
    insertion_idx = 0
    for i in range(len(box)):
        if box[i] != None:
            if box[i][0] == label:
                insertion_idx = i
                break
            insertion_idx = i + 1
    box[insertion_idx] = (label, value)


def remove_from_box(box, label):
    for i in range(len(box)):
        if box[i] != None and box[i][0] == label:
            box[i] = None
            insertion_idx = i
            for j in range(i + 1, len(box)):
                if box[j] != None:
                    box[insertion_idx] = box[j]
                    box[j] = None
                    insertion_idx += 1


def part_2():
    hashmap = [[None for _ in range(9)] for _ in range(256)]
    for s in initialization_seq:
        label = s[:2]
        operation = s[2]
        if operation == "-":
            box = hashmap[hash_string(label)]
            remove_from_box(box, label)
        elif operation == "=":
            value = int(s[3:])
            box = hashmap[hash_string(label)]
            add_to_box(box, label, value)

    print(hashmap)
    print(get_focusing_power(hashmap))

part_2()
