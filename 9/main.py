
with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def triangulate(history):
    inputs = []
    current_input = history.split()
    while any(char != '0' for char in current_input):
        next_input = []
        for i in range(len(current_input) - 1):
            next_input.append(int(current_input[i + 1]) - int(current_input[i]))
        inputs.append(current_input)
        current_input = next_input

    return inputs


def part_1():
    res = 0
    for history in lines:
        inputs = triangulate(history)

        s = 0
        for i in range(len(inputs) - 1, -1, -1):
            s += int(inputs[i][-1])
        print(f"history {history} has extrapolated value {s}")
        res += s

    print(res)
    return res


def part_2():
    res = 0
    for history in lines:
        inputs = triangulate(history)

        current_val = 0
        for i in range(len(inputs) - 1, -1, -1):
            current_val = int(inputs[i][0]) - current_val

        print(f"history {history} has extrapolated value {current_val}")
        res += current_val

    print(res)
    return res

part_2()
