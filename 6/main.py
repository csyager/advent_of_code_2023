from math import sqrt, ceil, floor

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def quadratic_solutions( a, b, c): 
 
    # calculating discriminant using formula
    dis = b * b - 4 * a * c 
    sqrt_val = sqrt(abs(dis)) 

    solution_1 = (-b + sqrt_val)/(2 * a)
    solution_2 = (-b - sqrt_val)/(2 * a)
    print(solution_1)
    print(solution_2)
    return solution_1, solution_2


def part_1():
    # parse input
    races = []
    for i in range(1, len(lines[0].split())):
        time = int(lines[0].split()[i])
        distance = int(lines[1].split()[i])
        races.append((time, distance))

    print(races)

    product = 1
    for time, distance in races:
        solution_1, solution_2 = quadratic_solutions(-1, time, (distance + 1) * -1)
        left = ceil(min(solution_1, solution_2))
        right = floor(max(solution_1, solution_2))

        print(left, right)
        product *= (right - left + 1)

    print(product)


def part_2():
    # parse input
    time = int(lines[0].split(":")[1].replace(" ", ""))
    distance = int(lines[1].split(":")[1].replace(" ", ""))

    solution_1, solution_2 = quadratic_solutions(-1, time, (distance + 1) * -1)

    left = ceil(min(solution_1, solution_2))
    right = floor(max(solution_1, solution_2))

    print(left, right)
    print(right - left + 1)

part_2()