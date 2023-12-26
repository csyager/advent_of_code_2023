from math import inf
from multiprocessing import Pool, Queue

class Range():
    def __init__(self, source_start, source_end, destination_start):
        self.source_start = source_start
        self.source_end = source_end
        self.destination_start = destination_start

    def __str__(self):
        return f"start: {self.source_start}, end: {self.source_end}, destination start: {self.destination_start}"

    def contains(self, key):
        if key >= self.source_start and key <= self.source_end:
            return True
        else:
            return False


class RangeDict():
    def __init__(self):
        self.ranges = []

    def get(self, key):
        for r in self.ranges:
            if r.contains(key):
                return r.destination_start + (key - r.source_start)
        return key

    def invert(self):
        res = RangeDict()
        for r in self.ranges:
            res.ranges.append(Range(r.destination_start, r.destination_start + (r.source_end - r.source_start), r.source_start))
        return res


with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

groups = []
current_lines = []
for line in lines:
    if line == "":
        groups.append(current_lines)
        current_lines = []
    else:
        current_lines.append(line)
groups.append(current_lines)

seeds = groups[0][0].split()[1:]

seed_to_soil = RangeDict()
soil_to_fertilizer = RangeDict()
fertilizer_to_water = RangeDict()
water_to_light = RangeDict()
light_to_temperature = RangeDict()
temperature_to_humidity = RangeDict()
humidity_to_location = RangeDict()

maps = [
    seed_to_soil,
    soil_to_fertilizer,
    fertilizer_to_water,
    water_to_light,
    light_to_temperature,
    temperature_to_humidity,
    humidity_to_location
]

for i in range(1, len(groups)):
    for mapping in groups[i][1:]:
        elements = mapping.split()
        dest_start = int(elements[0])
        source_start = int(elements[1])
        r = int(elements[2])
        maps[i - 1].ranges.append(Range(source_start, source_start + r - 1, dest_start))


def part_1():

    min_location = inf
    for seed in seeds:
        soil = seed_to_soil.get(int(seed))
        fertilizer = soil_to_fertilizer.get(soil)
        water = fertilizer_to_water.get(fertilizer)
        light = water_to_light.get(water)
        temperature = light_to_temperature.get(light)
        humidity = temperature_to_humidity.get(temperature)
        location = humidity_to_location.get(humidity)

        print(f"seed {seed}, soil {soil}, fertilizer {fertilizer}, water {water}, light {light}, temperature {temperature}, humidity {humidity}, location {location}")

        min_location = min(min_location, location)

    print(min_location)
    return min_location


soil_to_seed = seed_to_soil.invert()
fertilizer_to_soil = soil_to_fertilizer.invert()
water_to_fertilizer = fertilizer_to_water.invert()
light_to_water = water_to_light.invert()
temperature_to_light = light_to_temperature.invert()
humidity_to_temperature = temperature_to_humidity.invert()
location_to_humidity = humidity_to_location.invert()

def part_2():

    location = 0
    ranges = []
    for i in range(0, len(seeds), 2):
        seed = int(seeds[i])
        r = int(seeds[i + 1])
        ranges.append(Range(seed, seed + r - 1, None))

    while True:
        humidity = location_to_humidity.get(location)
        temperature = humidity_to_temperature.get(humidity)
        light = temperature_to_light.get(temperature)
        water = light_to_water.get(light)
        fertilizer = water_to_fertilizer.get(water)
        soil = fertilizer_to_soil.get(fertilizer)
        seed = soil_to_seed.get(soil)

        
        for r in ranges:
            if r.contains(seed):
                print(location)
                return location
        location += 1

part_2()
