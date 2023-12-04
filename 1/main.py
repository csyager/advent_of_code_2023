with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def part_1():
    s = 0

    for line in lines:
        print(line)
        left = 0
        right = len(line) - 1
        while not line[left].isdigit():
            left += 1
        while not line[right].isdigit():
            right -= 1
        val = int(line[left] + line[right])
        print(val)
        s += val

    print(s)

def part_2():
    s = 0
    num_strs = {
        'one': '1', 
        'two': '2', 
        'three': '3', 
        'four': '4', 
        'five': '5',
        'six': '6',
        'seven': '7', 
        'eight': '8', 
        'nine': '9'
    }
    for line in lines:
        nums = []
        for i, char in enumerate(line):
            for num in num_strs.keys():
                if num in line[i:i + len(num)]:
                    nums.append(num_strs[num])
            if char.isdigit():
                nums.append(char)
        s += int(nums[0] + nums[-1])
                
    print(s)  

# part_1()
part_2()