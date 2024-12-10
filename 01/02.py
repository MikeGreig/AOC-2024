def get_frequency_map(locations) -> dict:
    frequency_map = {}
    for loc in locations:
        if not frequency_map.get(loc):
            frequency_map[loc] = 1
        else: frequency_map[loc] += 1
    return frequency_map

input_pairs = [[line.split()[0], line.split()[1]] for line in open("input.txt")]
list_a, list_b = sorted(([int(pair[0]) for pair in input_pairs])), sorted([int(pair[1]) for pair in input_pairs])
frequency_map_a, frequency_map_b = get_frequency_map(list_a), get_frequency_map(list_b)

distance = 0
for loc, frequency in frequency_map_a.items():
    pair_distance = frequency * frequency_map_b.get(loc, 0)
    distance += loc * pair_distance
print(distance)






